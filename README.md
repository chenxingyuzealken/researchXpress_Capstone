<p align="center">
  <img src="images/temp_logo.png">
</p>

## Table of Contents

-   [💡 Overview ](#-overview)
-   [🖥 Tech Stack](#-tech-stack)
-   [🔧 Running The Dashboard](#-running-the-dashboard)
-   [📄 Pages](#-pages)
-   [✅ Testing ](#-testing)
-   [🫂 Team](#-team)

## 💡 Overview

Psychological researchers face a demanding and laborious process as they painstakingly review academic articles to determine their relevance and then manually combine the research findings. This process is time-consuming and can be quite taxing.

As the Dev who took over, I'll be maintaining the code until Feb 2026

## 🖥 Tech Stack

<div>
	<img height="60" width="60" src="images/icons/python.svg" alt="Python" title="Python"/>
	<img height="60" width="80" src="images/icons/streamlit.png" alt="Streamlit" title="Streamlit"/>
	<img height="60" width="100" src="images/icons/langchain.png" alt="Langchain" title="Langchain"/>
	<img height="60" width="90" src="images/icons/chroma.png" alt="Chroma" title="Chroma"/>
</div>

## 🔧 Running The Dashboard

### Prerequisite

-   Python should have been installed
-   Ideally a virtual environment should be created
-   This version is deployed on streamlit cloud, but there is no reason to believe that the user cannot run it on their software

### Install all the relevant libraries

```
pip install -r requirements.txt

```

### Launching the dashboard

```
streamlit run Home.py

```

### Exiting the dashboard

```
ctrl + c

```

For more information please visit <a href= 'https://drive.google.com/file/d/1k0HyC_L48_ePKt85Qj-gdVRvASWIxHNr/view?usp=sharing'>here [Dev note, this is outdated, to patch]</a>

## 📄 Pages

### 🏘 Home Page

<img src="images/ss/home_page.png" alt="Home Page" title="Home Page"/>
<br/>

### 🔑 User Guide Page

<img src="images/ss/user_guide.png" alt="User Guide Page" title="User Guide Page"/>
<br/>

### 📗 Excel Filtering Page

Filter an excel file of articles with a research prompt and view results

<img src="images/ss/excel_filtering.png" alt="Excel Filtering Page" title="Excel Filtering Page"/>
<br/>

### ☺️ My Collections Page

Create your own collection of pdfs with a few clicks

<img src="images/ss/my_collections.png" alt = "My Collections Page" title="My Collections Page"/> <br/>

### 📂 PDF Filtering Page

Filter a folder of PDF articles with a yes/no research prompt and view results

<img src="images/ss/pdf_filtering.png" alt = "PDF Filtering Page" title="PDF Filtering Page"/> <br/>

### 🔍 PDF Analysis Page

Query PDF articles with a research prompt

<img src="images/ss/pdf_analysis.png" alt = "PDF Analysis Page" title="PDF Analysis Page"/>
<br/>

### 📊 Usage Tracking Page

Track your LLM model usage

<img src="images/ss/usage_tracking.png" alt = "Usage Tracking Page" title="Usage Tracking Page"/>
<br/>

## ✅ Testing

Test Data has been provided under the **test_data** folder in the repo

The following files have been included in the **test_data** folder:

1. Excel file for the 📗 **Excel Filtering Page**
2. Zip file of PDFs for the ☺️ **My Collections Page** to create a collection
    - Creating a sample collection is **essential** for the 📂 **PDF Filtering** and 🔍 **PDF Analysis** pages

Sample prompts that can be used:

1.  **"Is the article relevant to psychological first aid?"** for

    -   📗 **Excel Filtering Page**
    -   📂 **PDF Filtering Page**

2.  **"How Is the article relevant to psychological first aid?"** for
    -   🔍 **PDF Analysis Page**

## 🫂 Former Team

<a href="https://github.com/hwhmervyn/researchXpress_Capstone/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hwhmervyn/researchXpress_Capstone" />
</a>
