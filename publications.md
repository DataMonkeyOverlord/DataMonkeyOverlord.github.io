---
layout: default
title: Publications
---

## 📚 Publications, Articles, and Patents 

### **[Project - Global Hunger Visualization Project ]**
Abdullah Adlouni
CSPB 3112 Professional Development 

Introduction
             This project’s goal was to learn about global hunger data (starvation, malnutrition levels and their relationship to a nations income and crop production) and its impact around the world while simultaneously learning about Azure Cloud resources, ETL processes, as well as, learn and implement the fundamental functions of data visualization leveraging Power Bi. 

 Background:
This project was a great opportunity to learn about cloud computing, cloud storage, data engineering and ETL processes. My focus at work is primarily on engineered component modeling, as we have a dedicated Data Engineer on our team. The project aimed to utilize the multiple services offered by Azure cloud in understanding the issues of food insecurity.  This project is important to me due to a transition of resources at work, we are about to start rolling out Azure cloud resources in my team. I haven’t had much exposure to Azure Data Lake, or Azure SQL Studio implementations prior to this project. Throughout this project I learned the basics of Azure cloud services, along with automating workflows into Azure Data Lake, and Azure Date Studio. Not everything went as planned, I did manage to learn how to setup alternative local MySQL instances such as Postgres and MySQL Workbench and learned to create a Dashboard in Power BI.
 
Methodology, Materials and Methods:

               I was lucky enough to have received direction from my co-worker Xua Dong to help guide my progress throughout this project. I had brief Bi-weekly 10–15-minute meetings with him to give me a general understanding of the direction the project was taking, along with how it would tie into our future infrastructure implementations at work. He directed me towards Azure documentation resources, YouTube videos (AZ-900 Azure Fundamentals via LinkedIn initially, which was later followed by multiple videos by Adam Marczak – Azure for Everyone),  
I focused on the following episodes: 
Episode 8 Resources, Resource groups & Resource Mangers
Episode 11 Azure Storage Services – Blob Storage, and Storage Tiers 
Episode 12 Database services Cosmos DB, SQL, MySQL and Postgres
Episode 23 Azure Firewall
Episode 29 Azure Resource Lock
Episode 30 Azure Resource Tags 
and future certification resources that would prove crucial to the project. As I progressed through my project, Xua Dong provided feedback pertaining to spinning up servers, ODBCs, Blob Service Client, that ultimately helped me pivot to reach my final goal of generating the desired dashboard in Power Bi. Obtaining the documentation and resources from Hua Dong was essential, it helped me really focus on procuring data for my visualization. Most of my learning is related to reading documentation, watching videos, as well as completion of DataCamp courses. Most of my time would primarily be focused on the setup of storage resources, pipeline creation, data mungning, and dashboard creation throughout this process. 
Results:
Setting up MySQL Workbench locally provided valuable insights into database management. I gained hands-on experience in creating databases and designing tables. I learned to leverage ODBC’s to transfer data into MySQL Workbench, I learned how to execute queries to create tables specifying the datatypes of my columns. The ODBC made the insertion of my batched data very convenient, given the size of the dataset it took a bit of time to load to the database. By leveraging Windows Task Scheduler, I was able to automate the process of refreshing data and pushing it to MySQL Workbench via ODBC. This automation improved efficiency and ensured updates are performed weekly upon the introduction of new files into my local directory. 
By effectively utilizing these tools and techniques, I was able to streamline my data pipeline and ensure that my MySQL Workbench database always contained the latest information that would feed my Power Bi visualization. This hands-on experience solidified my understanding of relational database concepts, SQL syntax, and data modeling techniques.

To automate the data extraction process from MySQL Workbench, I utilized Power BI’s local refresh capability. I learned to create and schedule dataflows, which automatically extracted, transformed, and loaded data from workbench into Power BI. This significantly reduced manual overhead and ensured data consistency and availability. I leveraged DAX, to create measures and create calculated columns, that enabled me to uncover insights hidden within the data. I implemented a vast array of visualization techniques, including bar charts, line charts, pie charts, and custom visuals, tailoring them to effectively design the dashboard seen below.

        The following dashboard focuses on six visualizations, the first highlights the average mortality per 1000 persons across all the nations of the world per continent. There are on average 183 mortalities per 1000 persons in the continent of Africa, while the average mortality rate in Europe on average is 14 persons. Drilling down into the countries that suffered from the highest mortality due to food insecurity, we see that 82% of Chads population suffer from moderate food insecurity. However, we cannot state the mortality rates are directly tied to food insecurity as such we investigate the percentage of the population that is malnourished and that percentage is 32%, inspecting further we see that of the children that are malnourished roughly 28% of them are stunted. 
One relationship we could establish is the negative correlation between GDP and rates of children stunted, and population that is malnourished. Food production has nearly tripled since 1991, from under 2 million tons produced annually to now roughly 6 million tons of food annually. Most of this population’s farming capacity is limited to essential grains such as Millet and Sorghum which are grown in the Sahel. These staples are consumed by local population of 16 million people, many of whom are displaced people who are refugees from nearby nations such as Sudan (Darfur Conflict), Central African Republic, Nigeria, and Libya 
Discussion and Reflection: 
Initially, the project aimed to leverage Azure cloud services, particularly Azure Data Lake and Power BI, to analyze and visualize global food insecurity data. However, due to budgetary constraints on my Azure Student account, a shift to a local MySQL Workbench instance became necessary. Despite this change, significant progress was made in understanding Azure architecture and data transfer processes. 

Key Milestones:
•	Setting up a local Azure Data Studio instance
•	Establishing a connection between the local instance and an Azure Storage account
•	Successfully transferring data between various environments, including the IDE, Azure Data Studio, and Azure Data Lake
•	Developed Python scripts to automate data ingestion and transformation tasks
•	Built interactive dashboards using Power BI
The project was a valuable learning experience. Despite the shift in approach, important milestones were met, including gaining proficiency in Azure architecture and data transfer methodologies. Establishing a local Azure Data Studio environment, along with successful data transfers between different platforms, has provided me a solid foundation for future Azure cloud-based projects. In the future I might consider focusing on a smaller sample set, compressing the dataset in the form of a parquet file, or consider tiered storage options. I would also consider the Azure Data Factory which might have been more ideal for transforming the data (bronze, silver, gold layers) ,data pipeline scheduling, and monitoring and management of the pipeline. 
Conclusion:
The project I had initially envisioned was within reach. I enjoyed learning about Azure and Power BI fundamentals this semester and will continue to expand my learnings into the future. Through this experience I have established a clear interest in furthering my understanding of data pipeline development and have a better understanding of ETL processes. Additionally, I hope to take the AZ-900 certification in the upcoming few weeks, which strengthened my understanding of cloud scalability, service models, and security. I plan on leveraging Azure Cognitive Search and Azure Machine Learning, to develop a component similarity tool. By utilizing these services, I can extract semantic meaning from component descriptions, and hope to generate vector representations, and perform efficient similarity searches. This will facilitate the identification of highly relevant components to those being prompted by leveraging GPT-4o. I hope to leverage Azure's scalable infrastructure and managed services to simplify the deployment and maintenance of such this project, to ensure consistent performance and reliability. 

References:
Data Sources:
UNICEF: 
Under-five_Mortality_Rates_2023: https://data.unicef.org/wp-content/uploads/2019/09/Under-five_Mortality_Rates_2023.xlsx
Under 5 Deaths: minimum-requirement-calories: https://data.unicef.org/wp-content/uploads/2019/09/Under-five_Deaths_2023.xlsx
World Food Program: 
https://www.wfp.org/publications/global-report-food-crises-grfc
Kaggle: 
Crop Statistics FAO – All Countries: https://www.kaggle.com/datasets/raghavramasamy/crop-statistics-fao-all-countries
Our World in Data: 
coefficient-of-variation-in-caloric-consumption-vs-gdp-per-capita:
https://ourworldindata.org/grapher/coefficient-of-variation-in-caloric-consumption-vs-gdp-per-capita 
share-of-population-with-moderate-or-severe-food-insecurity: https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/212-prevalence-of-moderate-or-severe-food-insecurity-in-the-population-based-on-the-food-insecurity-experience-scale/en
share-of-children-younger-than-5-who-suffer-from-stunting: https://data.who.int/indicators/i/A5A7413/5F8A486#:~:text=Worldwide%2C%20the%20prevalence%20of%20stunting,%25%20%2D%2022.9%25%5D%20in%202022
share-of-children-with-a-weight-too-low-for-their-height-wasting:
https://ourworldindata.org/grapher/share-of-children-with-a-weight-too-low-for-their-height-wasting
share-of-children-underweight:
https://ourworldindata.org/grapher/share-of-children-underweight
Documentation: 
Intro to Azure Data Lake Storage:https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
Power Bi : https://learn.microsoft.com/en-us/power-bi/
PostGres: https://www.postgresql.org/docs/
MySQL Workbench: https://dev.mysql.com/doc/
Video Resources: 
Adamn Marczak – Azure for Everyone: https://www.youtube.com/watch?v=NPEsD6n9A_I&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM
Episode 8 Resources, Resource groups & Resource Mangers 
https://www.youtube.com/watch?v=gIhf-S7BCdo
Episode 11 Azure Storage Services – Blob Storage, and Storage Tiers 
https://www.youtube.com/watch?v=_Qlkvd4ZQuo
Episode 12 Database services Cosmos DB, SQL, MySQL and Postgres
https://www.youtube.com/watch?v=RqD4nMyBazU
Episode 23 Azure Firewall
 https://www.youtube.com/watch?v=VIEaz869njk&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM&index=24
Episode 29 Azure Resource Lock 
 https://www.youtube.com/watch?v=eDH20Ve0eI0
Episode 30 Azure Resource Tags 
https://www.youtube.com/watch?v=J40eJR4qQ0w
DataCamp Course References: 
Power BI Fundamentals
https://www.datacamp.com/tracks/power-bi-fundamentals
Introduction to Dax in Power BI 
https://www.datacamp.com/courses/dax-functions-in-power-bi
Data Connections in Power BI
https://www.datacamp.com/courses/data-connections-in-power-bi
Reports in Power BI
https://www.datacamp.com/courses/reports-in-power-bi

Github Website - https://datamonkeyoverlord.github.io/



