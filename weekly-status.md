---
layout: default
title: Weekly Status Update
---

# 🗓️ Weekly Status Update - [9/3]

## What Did I Do Last Week?

- **Completed:** 1) Completed Proposal
                 2) I was reading documentation on Azure sql storage spin up
                 3) Setting up my Github Website 
- **Progress:** I am currently still working on my website, and I was able to read the documentation to setup the storage.

## What Do I Plan to Do This Week?

- **Upcoming Tasks:** Upcoming Goals is to setup the Website and Finish Populating it.
- **Focus Areas:** If time permits i will begin work on spinning up the azure storage

## Are There Any Impediments in My Way?

- **Challenges:** I am not familiar with github in the sense of formatting these webpages. 
- **Requests:** I believe further reading of the documentation will help clarify.

## Reflection on the Process

- **What Went Well:** I believe being able to have a proposal completed will help guide my learnings this semester.
- **Improvements:** I might need to gather more documentation and video resources before starting a process.
- **Lessons Learned:** I've learned to take better documentation.

---

![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [9/17]

## What Did I Do Last Week?

- **Completed:** 
  1) Prepared my github website for use
  2) Read through documentation to install my azure studio.
  3) Prepared documentation to access SQL resources, and Azure Resources.
- **Progress:** So i was out of town on my Honeymoon last week, so i dedicated alot of my time before my trip to prepare for this weeks work. 
   I am currently seeking data sources for food insecurity data. 

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
  Search for global food insecurity data source (Scrape for data if needed)
  Clean Data 
  Perform preliminary exploratory data analysis 
  Azure Studio installed  
  
- **Focus Areas:** If time permits Setup Azure Storage to pass data to the cloud from my work being done in azure studio  

## Are There Any Impediments in My Way?

- **Challenges:** Data Cleaning and ETL issues 
- **Requests:** None

## Reflection on the Process

- **What Went Well:** Having a stable internet connection is going to make work this week easier
- **Improvements:** Having a secure internet connection
- **Lessons Learned:** Not all data sources are created equal

---

![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
# 🗓️ Weekly Status Update - [9/24]

## What Did I Do Last Week?

- **Completed:** 
  1) Searched for Food Insecurity Data (Main Sources are Kaggle, Humdata)
     - World Food Programme 
       - Global Food Prices 
     - IPC (Integrated Food Security Phase Classification) 
           - Provides current state of Nations Food Security Classfication
               -  (Chronic Food Insecurity Classfication)
               -  (Acute Food Insecurity Classfication)
               -  (Acute Malnutrition Classification) 
       
     - USAid.gov 
     - Foodbank of the word dataset : 
          - Crop Yields Dataset
          - Livestock Yield Dataset   
          - Farm Worker Dataset
            
  3) Installed my azure studio.
  4) Currently Working on Data Cleansing and Normalization
- **Progress:** The datasets seem to be pretty sparse for what i am attempting to do. I am still working on cleaning and normalizing the datasets. 
   There appear to be many low quality data attributes given the lack of overlapping attibutes outside of year,country,city,major food category. 
   

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
  COntinue Data Normalization Tasks along 
  Perform preliminary exploratory data analysis 
  
- **Focus Areas:** Continued Data Normalization work

## Are There Any Impediments in My Way?

- **Challenges:** Alot of Data is in foreign languages.. looking at data in english is quite limiting.
- **Requests:** None

## Reflection on the Process

- **What Went Well:** Finding initial datasets to aggregate to use in my visualization and modeling efforts 
- **Improvements:** i will continue to search for additional data sources even as i work through the normalization efforts in the hope of producing a better output.
- **Lessons Learned:** cleaning datasets isnt fun.

---

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
# 🗓️ Weekly Status Update - [10/01]

## What Did I Do Last Week?

- **Completed:** 
  1) Cleaned Primary Dataset
  2) Performed preliminary data exploration 
     - Removed 20,000 Nan / non useful observations
     - identified abnormal data such as years with - values
     - normalized nan data with median values
     - clipped extreme outlier data
  3) Read Documentation on Azure DataLake Storage Setup
  4) Currently working on alternative data smoothing, and possibly binning values across the dataset.
  5) 
- **Progress:** Ive reduced many unneeded values out of my dataset. The dataset comprised roughly 25 tables that contained relevant data. 
After cleaning i ended up dropped many of the tables due to the inability to reconcile many of the obeservations and or not providing data that would be contiguious through
the period of the study. This resulted in roughly 9 dataframes that would be combined to form one of the main tables that will be moved into the data lake. 
This dataset was reduced from 130,000 observations down to 15,500 observations.  
The remaining supporting tables require further cleaning but are pretty close to completion as well. The remaining tables are roughly 2.2 million observations, which will provide me with 
additional data to support my visualizations.    

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
  Perform Datatransformation on the larger datasets  
  I will then create the tables in Azure SQL that i want to load the data into. 
  This will offer better control and checks on future entries or addition into the tables. 
  For example adding observations for columns that will not allow nulls will be rejected. 
   

- **Focus Areas:** Continued Data Normalization work

## Are There Any Impediments in My Way?

- **Challenges:** None
- **Requests:** None

## Reflection on the Process

- **What Went Well:** Cleaning the primary dataset went well
- **Improvements:** Transforming Observations into useable observations is critical to enlarging a dataset without causing duplications.
- **Lessons Learned:** Not all Datasets are created equal

---

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

