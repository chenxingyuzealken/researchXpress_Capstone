from langchain.schema.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.callbacks import get_openai_callback
import time

import sys,os
workingDirectory = os.getcwd()
costDirectory = os.path.join(workingDirectory, "cost_breakdown")
analysisDirectory = os.path.join(workingDirectory, "Analysis")

from llmConstants import chat

sys.path.append(costDirectory)
from update_cost import update_usage_logs, Stage

sys.path.append(analysisDirectory)
#from Individual_Analysis import cleaned_findings_df

# Patch the method
from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult

# Helper function to safely convert complex objects to standard types
def convert_to_standard_type(value):
    if hasattr(value, "__dict__"):
        return {k: convert_to_standard_type(v) for k, v in value.__dict__.items()}
    elif isinstance(value, list):
        return [convert_to_standard_type(item) for item in value]
    elif isinstance(value, dict):
        return {k: convert_to_standard_type(v) for k, v in value.items()}
    else:
        return value

# Override the `_combine_llm_outputs` method
def patched_combine_llm_outputs(self, llm_outputs):
    overall_token_usage = {}
    for output in llm_outputs:
        token_usage = output.get("token_usage", None)
        if token_usage is not None:
            for k, v in token_usage.items():
                # Convert both key and value to standard types if needed
                k = convert_to_standard_type(k)
                v = convert_to_standard_type(v)
                if k in overall_token_usage:
                    # Safely add values if they are numerical, else skip
                    try:
                        overall_token_usage[k] += v
                    except TypeError:
                        # Handle non-numeric types gracefully
                        pass
                else:
                    overall_token_usage[k] = v
    return {"token_usage": overall_token_usage}

# Patch the method in ChatOpenAI
ChatOpenAI._combine_llm_outputs = patched_combine_llm_outputs

# Function to get common themes
def get_common_themes(df, llm):
    df = df[df["Answer"].str.lower() == "yes"]
    docs = df['Findings'].apply(lambda x: Document(page_content=x[4:])).tolist()

    map_template = """The following is a set of documents
    {docs}
    Based on this list of docs, please identify the main themes'
    Helpful Answer:"""
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)

    reduce_template = """The following is set of summaries:
    {doc_summaries}
    Take these and distill it into a final, consolidated summary of the main themes'. 
    Helpful Answer:"""
    reduce_prompt = PromptTemplate.from_template(reduce_template)
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain, document_variable_name="doc_summaries"
    )

    reduce_documents_chain = ReduceDocumentsChain(
        combine_documents_chain=combine_documents_chain,
        collapse_documents_chain=combine_documents_chain,
        token_max=4000,
    )

    map_reduce_chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        reduce_documents_chain=reduce_documents_chain,
        document_variable_name="docs",
        return_intermediate_steps=False,
    )

    with get_openai_callback() as usage_info:
        result = map_reduce_chain.invoke({"input_documents": docs})

        total_input_tokens = usage_info.prompt_tokens
        total_output_tokens = usage_info.completion_tokens
        total_cost = usage_info.total_cost

        print(result, total_input_tokens, total_output_tokens, total_cost)
        output_text = result.get('output_text', 'No output text found')
    
        print(output_text)  # Print only the output_text
        return output_text  # Return only the output_text


def agg_analysis_main(cleaned_findings_df, progressBar1):
    PARTS_ALLOCATED_IND_ANALYSIS = 0.5
    PARTS_ALLOCATED_AGG_ANALYSIS = 0.3
    
    progressBar1.progress(PARTS_ALLOCATED_IND_ANALYSIS, text=f"Aggregating key themes...")
    result_tup = get_common_themes(cleaned_findings_df, chat)
    common_themes = result_tup
    progressBar1.progress(PARTS_ALLOCATED_AGG_ANALYSIS+PARTS_ALLOCATED_IND_ANALYSIS, text=f"Aggregating key themes...")
    time.sleep(1)

    return common_themes