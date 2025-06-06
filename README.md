This readme file was generated on [YYYY-MM-DD] by Yiduo Wang.

*Note:
[text within square brackets should be changed to specific information about your dataset.]
*help text within asterisks should be deleted before finalizing your document**

# GENERAL INFORMATION

Title: Cross-Platform Rankings of U.S. Liberal Arts Colleges: A Unified Dataset (2024)

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
- Data was collected by scraping publicly available ranking websites:
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
- Institutional names were standardized across sources to ensure accurate merging. Matching accuracy was manually verified using location information to resolve naming inconsistencies.

## Additional Related Data (Not Included)
Raw ranking data files scraped from each source website were collected during the project but are not included in this release. Only one file is included in this dataset. It represents the final merged and cleaned version derived from the sources listed above. The raw files were used solely to construct the merged dataset.

## Version Information
- **Number of versions:** 1  
- **Last updated:** 2025-06-06 
- No prior versions exist.

# METHODOLOGICAL INFORMATION

## Description of methods used for collection/generation of data: 
# Dataset Description

## Description of Methods Used for Data Collection and Generation

Raw data was collected through a combination of web scraping, direct downloads, and automated tools to compile college ranking information from multiple publicly available sources.

- **U.S. News & World Report** rankings were scraped using a publicly available Python scraper ([kajchang/USNews-College-Scraper](https://github.com/kajchang/USNews-College-Scraper)) that automates extraction of college rankings and metadata directly from the U.S. News website.

- **Academic Influence** and **Degree Choices** rankings were collected using custom Python scripts leveraging libraries including `selenium` and `BeautifulSoup` . Sample code demonstrating the Academic Influence data scraping process is shown below:

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


## Methods for processing the data: 
*describe how the submitted data were generated from the raw or collected data*

## Instrument- or software-specific information needed to interpret the data: 
*include full name and version of software, and any necessary packages or libraries needed to run scripts*

*include any additional methodological information needed to interpret and/or use the data, as appropriate*
* Standards and calibration information, if appropriate: 
* Environmental/experimental conditions: 
* Describe any quality-assurance procedures performed on the data: 
* People involved with sample collection, processing, analysis and/or submission: 


# DATA-SPECIFIC INFORMATION FOR `final_lac_data.csv`
* Number of variables: 85
* Number of cases/rows: 
* Variable List: *list variable name(s), description(s), unit(s) and value labels as appropriate for each*
* Missing data codes: *list code/symbol and definition*
* Specialized formats or other abbreviations used: 
