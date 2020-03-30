# 20 440 Project:

## Identifying biomarkers for traumatic brain injury-induced dementia using PLSDA on patient RNA-seq data

Itai Levin and Erin Tevonian

**Overview**

Here, you can find the source data and initial code for a study
investigating biomarkers of traumatic brain injury (TBI)-induced
dementia.

This code extracts data from an RNA-seq dataset and generates a heatmap to display normalized gene expression change levels






**Data**

The dataset is composed of brain RNA-seq data from 377 patients
containing the expression levels of 50,281 genes. Additional metadeta
includes patient information such as age, race, education levels,
and disease diagnosis.

 *Source:* The Allen Institute Aging, Dementia and Traumatic Brain Injury Study (2016):

 https://aging.brain-map.org/download/index


**Folder Structure**

*Dataset*: Contains RNA-seq CSV file: fpkm _file_normalized

This includes normalized fragments per kilobase per million mapped reads

*Code*: This folder contains Python code used for preprocesing and initial figure generation

*Figure*: This folder contains the output of the Python code, a heatmap of the normalized
fold change in gene expression

**Installation**

Code was generated using Python 3.7
as well as the packages numpy, pandas, and matplotlib
