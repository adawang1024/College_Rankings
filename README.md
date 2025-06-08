This readme file was updated on 2025-06-08 by Yiduo Wang.

# Cross-Platform Rankings of U.S. Liberal Arts Colleges: A Unified Dataset (2024)

# GENERAL INFORMATION

## Author/Principal Investigator Information
Name: Brian Brubach
ORCID:
Institution: Wellesley College
Address: 
Email: bb100@wellesley.edu

## Author/Associate or Co-investigator Information
Name: Yiduo Wang
ORCID:
Institution: Wellesley College
Address: 
Email: yw103@wellesley.edu


# DATA & FILE OVERVIEW

## Overview
This dataset provides a merged view of liberal arts college rankings in the United States, compiled from five publicly available sources. The data collection occurred between June and July 2024 and includes school-level ranking positions along with basic metadata (e.g., institution name, state, tuition, and enrollment).

## File List
- `final_lac_data.csv` – Final merged dataset containing ranking data from multiple sources (Academic Influence, Degree Choices, U.S. News, Washington Monthly, and WSJ/THE) for U.S. liberal arts colleges.

## Data Collection
- **Date of data collection:** 2024-06 to 2024-07  
- Ranking data was collected by scraping publicly available ranking websites:
	-  **Academic Influence Ranking**  
	  [https://academicinfluence.com/custom-college-rankings?rank=concentrated&level=bachelor&national=no&community=no&specialFocus=no#search-results](https://academicinfluence.com/custom-college-rankings?rank=concentrated&level=bachelor&national=no&community=no&specialFocus=no#search-results)
	
	- **Degree Choices Ranking**  
	  [https://www.degreechoices.com/best-colleges/rankings/liberal-arts/](https://www.degreechoices.com/best-colleges/rankings/liberal-arts/)
	
	- **U.S. News & World Report: National Liberal Arts Colleges Rankings**  
	  [https://www.usnews.com/best-colleges/rankings/national-liberal-arts-colleges?_sort=rank&_sortDirection=asc](https://www.usnews.com/best-colleges/rankings/national-liberal-arts-colleges?_sort=rank&_sortDirection=asc)
	
	- **Washington Monthly Liberal Arts College Rankings (2024)**  
	  [https://washingtonmonthly.com/2024-college-guide/liberal-arts/](https://washingtonmonthly.com/2024-college-guide/liberal-arts/)
	
	- **Wall Street Journal/Times Higher Education Liberal Arts Rankings (2022)**  
	  [https://www.timeshighereducation.com/student/best-universities/best-liberal-arts-colleges-united-states](https://www.timeshighereducation.com/student/best-universities/best-liberal-arts-colleges-united-states)
	
- College information was collected from the College Scorecard project (June 2024), developed by the U.S. Department of Education. The project includes institution-level data, offering insights into both overall institutional characteristics and specific fields of study. This dataset focuses on institution-level variables.

## Additional Related Data (Not Included)
Raw ranking data files scraped from each source website were collected during the project but are not included in this release. Only one file is included in this dataset. It represents the final merged and cleaned version derived from the sources listed above. The raw files were used solely to construct the merged dataset.

## Version Information
- **Number of versions:** 1  
- **Last updated:** 2025-06-08
- No prior versions exist.

## Description of Methods Used for Data Collection 

Raw data was collected through a combination of web scraping, direct downloads, and automated tools to compile college ranking information from multiple publicly available sources.

- **U.S. News & World Report** rankings were scraped using a publicly available Python scraper ([kajchang/USNews-College-Scraper](https://github.com/kajchang/USNews-College-Scraper)) that automates extraction of college rankings and metadata directly from the U.S. News website.

- **Academic Influence** and **Degree Choices** rankings were collected using Python scripts leveraging libraries including `selenium` and `BeautifulSoup`. Sample code demonstrating the Academic Influence data scraping process is shown below:

  ```python
	import requests
	from bs4 import BeautifulSoup
	import csv
	
	def fetch_college_data(page=None):
	    if page:
	      ### influence
	        url = f'https://academicinfluence.com/custom-college-rankings?level=bachelor&page={page}&national=no&community=no&specialFocus=no'
	        ### concentrated influence
	        # url = f'https://academicinfluence.com/custom-college-rankings?rank=concentrated&level=bachelor&page={page}&national=no&community=no&specialFocus=no'
	
	    else:
	      ### influence
	        url = 'https://academicinfluence.com/custom-college-rankings?level=bachelor&national=no&community=no&specialFocus=no'
	        ### concentrated influence
	        # url = "https://academicinfluence.com/custom-college-rankings?rank=concentrated&level=bachelor&national=no&community=no&specialFocus=no"
	
	    response = requests.get(url)
	    response.raise_for_status()
	    return response.text
	
	def parse_college_data(html):
	    soup = BeautifulSoup(html, 'html.parser')
	    colleges = []
	
	    # Adjusted selectors based on the provided HTML structure
	    for college in soup.select('div.school-card'):
	        ranking = college.select_one('div.school-card__rank').text.strip().replace("#","")
	        name = college.select_one('h3.school-card__school-name a').text.strip()
	        # print(name)
	        colleges.append((name, ranking))
	
	    return colleges
	
	def scrape_all_colleges(max_pages=25):
	    all_colleges = []
	    for page in range(max_pages + 1):
	        html = fetch_college_data(page if page >= 1 else None)
	        colleges = parse_college_data(html)
	        if not colleges:
	            break
	        all_colleges.extend(colleges)
	
	    return all_colleges
	
	def save_to_csv(colleges, filename='LAC by Influence.csv'):
	    with open(filename, mode='w', newline='', encoding='utf-8') as file:
	        writer = csv.writer(file)
	        writer.writerow(['Ranking', 'College Name'])
	        for college in colleges:
	            writer.writerow([college[1], college[0]])
	
	# Scrape all colleges and save to CSV
	all_colleges = scrape_all_colleges()
	
	# Save results to CSV
	save_to_csv(all_colleges)
  
- **Washington Monthly** rankings were downloaded directly from the official website’s 2024 Liberal Arts Colleges guide ([washingtonmonthly.com](https://washingtonmonthly.com/2024-college-guide/liberal-arts/)). The data was originally provided in Excel format and was converted to CSV during the data merging process.

- **Times Higher Education** rankings were collected using the Chrome browser extension *Instant Data Scraper*, which automated extraction of structured table data from the 2022 Best Liberal Arts Colleges in the United States webpage ([timeshighereducation.com](https://www.timeshighereducation.com/student/best-universities/best-liberal-arts-colleges-united-states)).



## Methods for processing the data: 
- An **outer merge** was used to combine data from multiple sources based on institutional name and state, preventing unintended exclusions.  
- Institutional names were standardized across datasets to support accurate merging.  
- Matching accuracy was manually verified using additional information—such as school websites—to resolve discrepancies and naming inconsistencies.

# DATA-SPECIFIC INFORMATION FOR `final_lac_data.csv`
* Number of variables: 85
* Number of cases/rows: 1278
## Core Dataset Variable Description
### Identifiers
- **Name**: Official institution name.
- **Standardized Name**: Cleaned and standardized institution name for consistency across datasets.

### Ranking Variables
- **Academic Influence Ranking (Concentrated Influence)**: Ranking based on Academic Influence ["Concentrated Influence"](https://academicinfluence.com/about/concentrated-influence) metrics (accessed in June 2024). 
- **Washington Monthly Ranking**: 2024 Liberal Arts Colleges Ranking published by Washington Monthly.
- **Times Higher Education Ranking (2022)**: Top 100 liberal arts colleges in the United States using data from the Wall Street Journal/Times Higher Education US College Rankings in 2022.
- **US News Ranking (with ties)**: 2024 liberal arts college ranking from U.S. News & World Report, including tied positions.  
  - *Special data codes:*  
    - **-2**: Institution is *unranked* by U.S. News.  
    - **-1**: Institution is ranked within a *range only* (e.g., #186–204) at the end, without a specific rank assigned.
- **Degree Choices Ranking**: Ranking of liberal arts colleges focused on relative financial value, as published by DegreeChoices (accessed in July 2024).
  
### School Information and Enrollment Demographics Variables
- **Pell Students**: Percentage of students receiving Pell grants.
- **UNITID**: Unique identification number assigned to postsecondary institutions as surveyed through IPEDS.
- **OPEID**: identification number used by the U.S. Department of Education's Office of Postsecondary Education (OPE) and Federal Student Aid Office (FSA).
- **URL**: Official college website URL.

#### Enrollment by Gender
- **Men Enroll**: Percentage of male enrolled students.
- **Women Enroll**: Percentage of female enrolled students.

#### Enrollment by Race/Ethnicity
- **White Enroll**: Percentage of enrolled white students.
- **Black Enroll**: Percentage of enrolled black students.
- **Hispanic Enroll**: Number of enrolled Hispanic students.
- **Asian Enroll**: Number of enrolled Asian students.
- **AI/AN Enroll**: Number of enrolled American Indian or Alaska Native students.
- **NH/PI Enroll**: Number of enrolled Native Hawaiian or Pacific Islander students.
- **2+ Races Enroll**: Number of students enrolled identifying with two or more races.
- **Non-Res Aliens Enroll**: Number of non-resident alien students enrolled.
- **Race Unkn Enroll**: Number of enrolled students with unknown race/ethnicity.

### Institutional Type & Designations
(For all variables below, 1 = Yes, 0 = No)  
- **Pub/Priv Type**: Classification as public or private institution.
- **HBCU**: Indicator for Historically Black Colleges and Universities.
- **PBI**: Indicator for Predominantly Black Institutions.
- **ANNHI**: Indicator for Alaska Native and Native Hawaiian-serving Institutions.
- **TRIBAL**: Indicator for Tribal Colleges and Universities.
- **AANAPII**: Indicator for Asian American-/Native American-Pacific Islander-serving Institutions;
- **HSI**: Indicator for Hispanic-serving Institutions.
- **NANTI**: Indicator for Native American Non-Tribal Institutions.

### Financial and Admission Metrics
- **Avg Cost (4yr)**: Average annual total cost—including tuition, fees, books, and living expenses—for full-time, first-time undergraduates receiving Title IV aid. *(COSTT4_A in original source)*  
- **Adm Rate**: Percentage of applicants admitted to the institution. *(ADM_RATE_ALL in original source)*  
- **Comp Rate (100%)**: Percentage of students completing their program within 100% of the expected time. *(C100_4 in original source)*  

## Additional Variables

Additional columns of institutional information from Washington Monthly, Times Higher Education, US News, and DegreeChoices are included for reference. However, to maintain consistency, this research primarily focuses on variables provided by the College Scorecard.

