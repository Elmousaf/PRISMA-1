# PRISMA-1
PRISMA Semi-Automated Workflow for Bibliographic Screening in Cardiovascular Diseases and Artificial Intelligence
Presentation

This repository contains the Python scripts and working files used to support a bibliographic selection process inspired by PRISMA guidelines. The project was designed to organize, merge, deduplicate, and pre-screen scientific articles related to cardiovascular diseases, artificial intelligence, machine learning, deep learning, and patient monitoring.

The workflow combines an initial filtering phase performed directly on bibliographic platforms, a structuring phase of references into a unified dataset, an automated deduplication step, and a thematic pre-selection based on inclusion and exclusion criteria. The objective is to provide a reproducible and traceable framework for the final full-text review of selected studies.

Objective of the Repository

This project aims to document and support a methodological approach for bibliographic screening. It enables:

importing references from PubMed and Scopus;
merging records into a single dataset;
detecting duplicates based on DOI, PMID, and titles;
applying automated pre-selection based on thematic keywords;
retaining relevant articles in a final file dedicated to manual review.

This repository serves as a decision-support tool and not as a replacement for scientific evaluation performed by the researcher.

Data Sources

The bibliographic references were identified from the following sources:

PubMed: 749 initially identified records;
Scopus: 192 initially identified records;
Other sources: 3 additional records added later.
Search Strategies

The searches were conducted using queries targeting cardiovascular diseases, artificial intelligence approaches, and patient monitoring.

PubMed
("Cardiovascular Diseases"[MeSH] OR "cardiovascular disease"[Title/Abstract] OR "heart disease"[Title/Abstract] OR "arrhythmia"[Title/Abstract]) 
AND ("machine learning"[Title/Abstract] OR "artificial intelligence"[Title/Abstract] OR "deep learning"[Title/Abstract]) 
AND ("risk"[Title/Abstract] OR "prediction"[Title/Abstract] OR "prognosis"[Title/Abstract] OR "early detection"[Title/Abstract] OR "risk stratification"[Title/Abstract]) 
AND ("patient monitoring"[Title/Abstract] OR "remote monitoring"[Title/Abstract] OR "continuous monitoring"[Title/Abstract] OR "real-time monitoring"[Title/Abstract] OR "telemonitoring"[Title/Abstract] OR "ambulatory monitoring"[Title/Abstract]) 
AND ("2016/01/01"[Date - Publication] : "2026/04/30"[Date - Publication]) AND (English[Language])
Scopus
TITLE-ABS-KEY ( "cardiovascular disease" OR "heart disease" OR "arrhythmia" ) 
AND TITLE-ABS-KEY ( "machine learning" OR "artificial intelligence" OR "deep learning" ) 
AND TITLE-ABS-KEY ( "risk" OR "prediction" OR "prognosis" OR "early detection" OR "risk stratification" ) 
AND TITLE-ABS-KEY ( "patient monitoring" OR "remote monitoring" OR "continuous monitoring" OR "real-time monitoring" OR "telemonitoring" OR "ambulatory monitoring") 
AND PUBYEAR > 2015 AND PUBYEAR < 2027 
AND ( LIMIT-TO ( LANGUAGE, "English" ))
Selection Criteria
Inclusion Criteria

Records were considered potentially eligible if they met one or more of the following criteria:

publication within the last ten years;
publication in English;
study conducted in a scientific context;
adult human population;
presence of keywords related to cardiovascular diseases;
presence of keywords related to artificial intelligence, machine learning, or deep learning;
relevance to monitoring, prediction, or decision support in cardiovascular healthcare.
Exclusion Criteria

Records were excluded if they met one or more of the following conditions:

animal studies or pediatric studies;
review articles or systematic reviews;
studies focused only on IoT, wearable devices (wearables, smartwatch, Apple Watch);
studies limited to patient monitoring without clinical relevance;
articles with unverifiable data or sources;
studies outside the scope (cardiovascular diseases, AI, ML, patient monitoring);
publications older than 10 years;
non-English publications.
Methodological Workflow

The general workflow follows these steps:

export of references from both platforms;
parsing and structuring into a unified Excel file;
merging references into a single dataset;
automatic duplicate detection;
application of inclusion and exclusion criteria;
relevance scoring of articles;
retention of selected articles for evaluation and reading;
full-text review and final selection;
addition of 3 supplementary references from other sources.
PRISMA Summary

A total of 941 records were identified from the main databases, including 192 from PubMed and 749 from Scopus.

After merging, 123 duplicates were identified, reducing the dataset to 818 records. The application of inclusion and exclusion criteria led to the removal of 730 records and the retention of 88 articles for screening. After full-text review, 39 articles were included. Three additional articles from other sources were added, resulting in a final corpus of 42 studies included in the review.

Project Structure
Python Scripts
Papers_Parsing.py
Imports and structures references from multiple sources and merges PubMed and Scopus exports into a unified Excel screening file.
RechercheDuplicates.py
Normalizes DOI, PMID, and titles to construct a deduplication key and generates a duplicate report.
CriteriaExclusion.py
Performs automated pre-screening using keyword-based rules and assigns preliminary decisions and scores.
ArticlesMaintenus.py
Filters retained articles based on relevance score (≥ 3) and generates the final dataset.
Final dataset after full-text review.
Data and Output Files
Pubmed1.txt — raw PubMed export
Scopus.csv — Scopus export
AffichageArticlesTotal.xlsx — merged screening dataset
Deduplicated_Final.xlsx — deduplication report
Filtered_Final_PRISMA_Strict.xlsx — scored dataset
ArticlesMaintenus.xlsx — retained articles
After review.xlsx — final included studies
Scoring Logic

The automated pre-selection is based on keyword lists related to:

cardiovascular diseases;
artificial intelligence, machine learning, and deep learning;
monitoring, telemedicine, and patient follow-up;
adult human population.

Animal studies are excluded. Each article receives a relevance score. Highly relevant studies are included, borderline cases are flagged for manual review, and low-relevance studies are excluded. The final filtering script retains articles with a score ≥ 3.

Requirements

Recommended environment:

Python 3.10 or later
pandas
openpyxl

Installation:

pip install pandas openpyxl
Usage
python Papers_Parsing.py
python RechercheDuplicates.py
python CriteriaExclusion.py
python ArticlesMaintenus.py
Limitations

This workflow is a support tool for screening and not a fully autonomous selection system. Final decisions must be validated through manual review of titles, abstracts, and full texts when necessary.

The scoring system is based on heuristic rules and keyword presence. It improves screening efficiency but does not replace methodological judgment.

Reproducibility

This repository aims to improve traceability and reproducibility of the screening process. However, results may vary depending on:

database query date;
applied filters;
export formats;
manual validation decisions;
updates in database content.
Citation

If you use or adapt this workflow for academic or scientific purposes, please cite the associated research work or explicitly reference this repository.
