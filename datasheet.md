# Datasheet for dataset "Cross-Platform Rankings of U.S. Liberal Arts Colleges: A Unified Dataset (2024)"
By: Yiduo Wang `<yw103@wellesley.edu>` and Brian Brubach `<bb100@wellesley.edu>`

As part of a study auditing new college ranking algorithms for potential bias and adverse impact, we collected and standardized a dataset of college rankings from multiple sources, including Degree Choices, Academic Influence, U.S. News, Washington Monthly, and Times Higher Education, along with institutional data from the U.S. Department of Education. We call this dataset the Cross-Platform Rankings of U.S. Liberal Arts Colleges dataset; what follows below is the datasheet describing this data. If you use this dataset, please acknowledge it by citing the associated research project or contacting the authors.


Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation

1. **For what purpose was the dataset created?** *(Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.)*
    
    The dataset was created to audit new college ranking algorithms—specifically Degree Choices and Academic Influence—for potential bias and disproportionate impact on underrepresented institutions. It integrates data scraped from these ranking websites with information from the U.S. Department of Education, covering 1278 colleges. This standardized dataset enables statistical analysis of ranking discrepancies and helps identify institutional factors associated with adverse impacts.


1. **Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?**
    
    The dataset was created by Yiduo Wang, an undergraduate student at Wellesley College at the time of creation, as part of a research project advised by Professor Brian Brubach in the Computer Science Department at Wellesley College.


1. **Who funded the creation of the dataset?** *(If there is an associated grant, please provide the name of the grantor and the grant name and number.)*
    
    ?


1. **Any other comments?**
    
    None.


## Composition

1. **What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?** *(Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.)*
    
    Each instance in the dataset represents a single U.S. liberal arts college included in at least one major college ranking.

2. **How many instances are there in total (of each type, if appropriate)?**
    
    The dataset contains 1278 rows, each representing one college.

3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** *(If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).)*
    
    The dataset is a sample of U.S. postsecondary institutions, limited to liberal arts colleges that appear in at least one of five selected ranking systems. It is not representative of the larger set, as it specifically focuses on liberal arts colleges. These schools are often overlooked or penalized in rankings that emphasize financial return, so this dataset is designed to explore how such rankings may reflect or reinforce bias against institutions with broader educational missions.

4. **What data does each instance consist of?** *(``Raw'' data (e.g., unprocessed text or images)or features? In either case, please provide a description.)*
    
    Each instance consists of features representing institutional characteristics. These include college rankings from five sources, demographic and financial data, enrollment statistics by gender and race, and institutional classifications. All variables are aggregated and cleaned from public sources. No raw or unprocessed data (e.g., text, images) are included; the dataset contains only derived features for quantitative analysis.

5. **Is there a label or target associated with each instance? If so, please provide a description.**
    
    No, this dataset is not designed for supervised learning and does not include an explicit label or target variable. The goal is to support exploratory analysis and audit the behavior and potential biases in various college ranking systems.


6. **Is any information missing from individual instances?** *(If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.)*
    
    Yes, some variables contain missing values because data was unavailable from the original sources. For example, not all schools appear in every ranking system, and some demographic or financial metrics are incomplete in government datasets. Missing data is left as-is to preserve transparency.


7. **Are relationships between individual instances made explicit (e.g., users' movie ratings, social network links)?** *( If so, please describe how these relationships are made explicit.)*
    
    No explicit relationships exist between instances. Each row represents a single institution and is treated independently.

8. **Are there recommended data splits (e.g., training, development/validation, testing)?** *(If so, please provide a description of these splits, explaining the rationale behind them.)*
    
    This dataset is not intended for model training or predictive tasks, so no training/validation/testing splits are provided. However, for analytical purposes, users may consider splitting institutions into tuition buckets. While this does not fully isolate tuition effects, it can help make the relationship between rankings and key characteristics—such as women’s enrollment—clearer by reducing the confounding influence of cost differences across institutions.


9. **Are there any errors, sources of noise, or redundancies in the dataset?** *(If so, please provide a description.)*
    
    Some data sources may contain inconsistencies such as differing naming conventions or rounding errors. We standardized institution names to reduce duplication and manually resolved a small number of inconsistencies. However, minor noise may remain, especially in scraped rankings and demographic figures.

10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?** *(If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.)*
    
   ///


11. **Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** *(If so, please provide a description.)*
    
    No. All data is from public sources, including federal government datasets (e.g., College Scorecard) and publicly available ranking websites. No confidential or proprietary data is included.


12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** *(If so, please describe why.)*
    
    No. The dataset includes only institutional-level information such as enrollment, graduation rates, and rankings. It does not contain any personal, emotional, or potentially offensive content.

13. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Indirectly. The dataset reflects attributes of institutions, but includes aggregated demographic data (e.g., gender, race) of student populations.

14. **Does the dataset identify any subpopulations (e.g., by age, gender)?** *(If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.)*
    
    Yes. The dataset includes institutional-level demographic breakdowns by gender and race/ethnicity. These are reported in aggregate and do not identify individuals.


15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** *(If so, please describe how.)*
    
    No. All data is at the institutional level and fully anonymized. No individual-level data is included.


16. **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** *(If so, please provide a description.)*
    
    It contains sensitive demographic and financial indicators in aggregate form, such as racial composition and Pell Grant recipient percentages. However, this information is publicly reported and aggregated at the institutional level.


17. **Any other comments?**
    
    None.



## Collection Process


1. **How was the data associated with each instance acquired?** *(Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.)*
    
    The ranking data for each college was directly collected from publicly available online sources. Degree Choices and Academic Influence rankings were scraped using Python scripts with Selenium and BeautifulSoup. U.S. News ranking was obtained via a public available Python scraper ([kajchang/USNews-College-Scraper](https://github.com/kajchang/USNews-College-Scraper)). Washington Monthly ranking was downloaded as spreadsheets from their website. Times Higher Education rankings were extracted using the Chrome extension Instant Data Scraper. All data were cleaned and matched to institutional records from the U.S. Department of Education to ensure consistency and accuracy.


1. **What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?** *(How were these mechanisms or procedures validated?)*
    
    Annotation was conducted using [TagEditor](https://github.com/d5555/TagEditor).


1. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?**
    
    See answer to question #2 in [Composition](#composition).


1. **Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?**
    
    All collection and annotation was done by the two authors.


1. **Over what timeframe was the data collected?** *(Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?  If not, please describe the timeframe in which the data associated with the instances was created.)*
    
    The dataset was collected in the early Summer of 2019, which does not necessarily reflect the timeframe of the data collected.


1. **Were any ethical review processes conducted (e.g., by an institutional review board)?** *(If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    No review processes were conducted with respect to the collection and annotation of this data (though review was done for other aspects of this work; see the paper linked at the top of the datasheet).


1. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Yes; the majority of the documents in the dataset are articles about people (either their Wikipedia entries or stories about them in periodicals).


1. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?**
    
    Other sources: Wikipedia and periodicals.


1. **Were the individuals in question notified about the data collection?** *(If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.)*
    
    No, they were not notified.


1. **Did the individuals in question consent to the collection and use of their data?** *(If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.)*
    
    No. All documents are public. In the case of the AO3 stories, we explicitly contacted the authors and received permission to use their stories. (Several authors we contacted did not respond; we did not include their stories.)


1. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** *(If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).)*
    
    N/A.


1. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?** *(If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    No. 


1. **Any other comments?**
    
    None.

   
## Preprocessing/cleaning/labeling

_The questions in this section are intended to provide dataset consumers with the information
they need to determine whether the “raw” data has been processed in ways that are compatible
with their chosen tasks. For example, text that has been converted into a “bag-of-words” is
not suitable for tasks involving word order._

### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

_If so, please provide a description. If not, you may skip the remainder of the questions in
this section._

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

_If so, please provide a link or other access point to the “raw” data._

### Is the software used to preprocess/clean/label the instances available?

_If so, please provide a link or other access point._

### Any other comments?

## Uses

_These questions are intended to encourage dataset creators to reflect on the tasks
for which the dataset should and should not be used. By explicitly highlighting these tasks,
dataset creators can help dataset consumers to make informed decisions, thereby avoiding
potential risks or harms._

### Has the dataset been used for any tasks already?

_If so, please provide a description._

### Is there a repository that links to any or all papers or systems that use the dataset?

_If so, please provide a link or other access point._

### What (other) tasks could the dataset be used for?

### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

_For example, is there anything that a future user might need to know to avoid uses that
could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of
service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please
provide a description. Is there anything a future user could do to mitigate these undesirable
harms?_

### Are there tasks for which the dataset should not be used?

_If so, please provide a description._

### Any other comments?

## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? 

_If so, please provide a description._

### How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?

_Does the dataset have a digital object identifier (DOI)?_

### When will the dataset be distributed?

### Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

_If so, please describe this license and/or ToU, and provide a link or other access point to,
or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated
with these restrictions._

### Have any third parties imposed IP-based or other restrictions on the data associated with the instances?

_If so, please describe these restrictions, and provide a link or other access point to, or
otherwise reproduce, any relevant licensing terms, as well as any fees associated with these
restrictions._

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

_If so, please describe these restrictions, and provide a link or other access point to, or otherwise
reproduce, any supporting documentation._

### Any other comments?

## Maintenance

_These questions are intended to encourage dataset creators to plan for dataset maintenance
and communicate this plan with dataset consumers._

### Who is supporting/hosting/maintaining the dataset?

### How can the owner/curator/manager of the dataset be contacted (e.g., email address)?

### Is there an erratum?

_If so, please provide a link or other access point._

### Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?

_If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?_

### If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?

_If so, please describe these limits and explain how they will be enforced._

### Will older versions of the dataset continue to be supported/hosted/maintained?

_If so, please describe how. If not, please describe how its obsolescence will be communicated to users._

### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

_If so, please provide a description. Will these contributions be validated/verified? If so,
please describe how. If not, why not? Is there a process for communicating/distributing these
contributions to other users? If so, please provide a description._

### Any other comments?
