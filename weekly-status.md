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

# 🗓️ Weekly Status Update - [10/08]

## What Did I Do Last Week?

- **Completed:** 
  I finished cleaning my dataset last week along with the reduction of the dataset.
  I also partook in a course in Microsoft Azure to help better understand Cloud Concepts.
  The course name: The Microsoft Azure Fundamentals (AZ-900) Cert Prep: 1 Cloud Concepts
  It highlighted cloud computing scalability, differences in cloud models, along with the shared security responsibility divided between cloud providers and users.  
- **Progress:** Ive reduced many unneeded values out of my dataset. The dataset comprised roughly 25 tables that contained relevant data. 
After cleaning i ended up dropped many of the tables due to the inability to reconcile many of the obeservations and or not providing data that would be contiguious through
the period of the study. This resulted in roughly 9 dataframes that would be combined to form one of the main tables that will be moved into the data lake. 
This dataset was reduced from 130,000 observations down to 15,500 observations.  
The remaining supporting tables require further cleaning but are pretty close to completion as well. The remaining tables are roughly 2.2 million observations, which will provide me with 
additional data to support my visualizations.    

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
  I have run into an impediment with my Azure cloud resource,  and my student access has been concluded. 
   

- **Focus Areas:** I'm currently looking into alternatives to azure sql server. 

## Are There Any Impediments in My Way?

- **Challenges:** Monetary impediments for credits in sql server , the worst case scenario will be that i might consider loading my Power BI dashboard with csv files rather than using triggers upon updating my sql tables.
- **Requests:** None

## Reflection on the Process
  I must consider alternative methods to Azure SQL. 
---

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [10/15]

## What Did I Do Last Week?

- **Completed:** 
      I primarily focused on searching for alternatives to Azure SQL DB, as well as taking an intro to Data Engineering course this week which highlighted the use of scheduling tools such as Airflow
 
- **Progress:**    Looking into Airflow 

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
   I plan to continue searching for methods by which to automate my workflow. 
   I am considering PostgreSQL as an alternative and plan to read through the documentation this week to create local database to use in my project.
   Based on the limited time available i surmise it be beneficial to avoid a sql database altogether and export files 
   i have cleaned in my IDE directly into a file to be imported into PowerBI. 
   

- **Focus Areas:** 

## Are There Any Impediments in My Way?

- **Challenges:** Limited Time, i have a business trip next week as well as an exam.
- **Requests:** None

## Reflection on the Process

- **What Went Well:** Looking into data engineering courses via datacamp has been very helpful in my path forward. I wish i had looked into this much sooner. 
- **Improvements:** 
- **Lessons Learned:**

---

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [10/22]

## What Did I Do Last Week?

- **Completed:** 
   I setup Postgres and have started pushing my data to the local database that i created. 

## What Do I Plan to Do This Week?
   
- **Upcoming Tasks:**
  I am planning to perform a test pull into power bi later this week once i return from my work conference. 

## Are There Any Impediments in My Way?

- **Challenges:** Being infront of my local PC 
- **Requests:** None

## Reflection on the Process

- **Lessons Learned:** Having setup the local database i hope that the pull into power bi should be smooth and i can attempt to focus on the visualization creation.
Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [10/29]

## What Did I Do Last Week?

- **Completed:** 
  I thought the transfer of data would be a bit easier than i anticipated. I have found out the hard way that table organization and syntax is different in postgre from what i picked up in Azure SQL.
  In order to get a better understanding of Postgres, ive taken a datacamp course focusing on creating Postgre SQL Databases in Datacamp.  
  The course focuses on 
      1) The Structure of PostgreSQL Databases - creating tables, naming tables, creating schemas, identifying user level schemas vs public schemas
      2) PostgreSQL Data Types 
      3) Database Normalization - NF1,NF2, NF3 
      4) Access Control in PostgreSQL - access control, creating new users, hierarchical access, etc   

## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
   I am planning to work through the issues with my odbc. 
  
- **Focus Areas:** Create my tables, along with the proper normalization of schemas, possibly start my PowerBi course in Datacamp 

## Are There Any Impediments in My Way?

- **Challenges:** None
- **Requests:** None

## Reflection on the Process
---

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
# 🗓️ Weekly Status Update - [11/05]

## What Did I Do Last Week?

- **Completed:** 
I dedicated quite a bit of time this week completing DataCamp's "Introduction to Power BI" course, which allowed me to explore data visualization this week. 
Data loading, transformation, and modeling are among the fundamental features of Power BI that I now have a firm grasp on. 
I learned how to use Power Query Editor to clean and shape data, and experimented with several visualization methods, such pie charts, line charts, and bar charts, to produce reports, based on the sample examples through DataCamp. 
I learned how to dynamically investigate data using slicers to gain deeper insights. 

## What Do I Plan to Do This Week?

- **Upcoming Tasks:** I plan to finish remaining sections of this course over the following week which highlights filtering.
   There is a section that covers Python in Power BI that i am very interested in doing as well. 

## Are There Any Impediments in My Way?

- **Challenges:** None
- **Requests:** 

## Reflection on the Process

- **What Went Well:**  I am hoping to bring all the pieces that ive learned together once ive finished this course to try some visualization together.
- **Improvements:** 
- **Lessons Learned:**

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
# 🗓️ Weekly Status Update - [11/12]

## What Did I Do Last Week?

- **Completed:** I have completed the Introduction to Power Bi course in data camp, 
                 I have attached a  tree map to illustrate an example of a visualization generated from the dataset provided by datacamp.
                 I did not have a chance to work on the Python in Power BI this week.

## What Do I Plan to Do This Week?

- **Upcoming Tasks:** 
- **Focus Areas:** Complete the Data Transformation in Power BI Course in Data Camp 
                    My plan is to explore advanced slicer use cases as well as different Tooltips and Drill through capabilities. 
## Are There Any Impediments in My Way?

- **Challenges:** None
- **Requests:** 

## Reflection on the Process

![image](https://github.com/user-attachments/assets/3f6ef92f-2623-4475-9c01-72f47d74152e)


---
![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
# 🗓️ Weekly Status Update - [11/26]

## What Did I Do Last Week?
## THANKSGIVING VACATION 
---

![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [12/3]

## What Did I Do Last Week?

- **Completed:** 
   Last Week was a week off for me, i spent a great deal of time with family, and have been preparing for finals in other classes as well. 
## What Do I Plan to Do This Week?

- **Upcoming Tasks:**
   I believe i should have my preliminary visualization setup this week. I hope that it will be as fruitful to see the data i worked so hard to clean.  
  
- **Focus Areas:** 

## Are There Any Impediments in My Way?

- **Challenges:** I am currently experiencing an issue establishing a connection to postgres via Power Bi Desktop. 
                  I have used the correct username and password but for whatever reason the connection wont establish. I think  i might have a work around...
- **Requests:** None

## Reflection on the Process

- **What Went Well:** I hope i have enough time to push through alot of my project this week so i  can make sure my report is polished.
                       I have a deadline at work that has been making me push alot of things here to the right but it should be over with by wednesday of next week.
- **Improvements:** 
- **Lessons Learned:**

---

![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!

# 🗓️ Weekly Status Update - [12/15]

## What Did I Do Last Week?

- **Completed:** 1) Completed MySQL Workbench Setup 
                 2) Completed Power BI Dashboard 
                 3) Completed Final Paper 
- **Progress:** 

## What Do I Plan to Do This Week?

- **Upcoming Tasks:** Finish Documentation 
- **Focus Areas:** If time permits i might try to fix my website 

## Are There Any Impediments in My Way?

- **Challenges:** I do not have a strong background in HTML and CSS
- **Requests:** None

## Reflection on the Process

- **What Went Well:** Finally completed my Dashboard containing multiple visualizations
- **Improvements:** I would consider learning embedding features to see if it is possible to embed my dashbaord into my website 
- **Lessons Learned:**
---

![Image](link-to-image-if-any) <!-- Optional: Add images if applicable -->

Thank you for reading this week's update. Feel free to reach out if you have any questions or feedback!
