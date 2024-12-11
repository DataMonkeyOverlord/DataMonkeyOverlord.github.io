# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:52:17 2024

@author: Musuki
"""
import pandas as pd
import os
import sys

# Specify the path where the CSV files are located
path = r"C:\Users\Musuki\OneDrive - UW\Desktop\CS3287_PROJECT\\"

# Create an empty list to hold dataframes
dataframes = []

for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    
    if file_name.endswith(".csv"):
        try:
            # Try reading the CSV with utf-8 encoding first
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            # If it fails, try using 'ISO-8859-1' (a common fallback encoding)
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
    else: 
        df = pd.read_excel(file_path)
                           
    dataframes.append(df)


### Combine Dataframes##

common_dfs = []
not_common_dfs = []

for df in dataframes:
    if all(col in df.columns for col in ['Entity', 'Year']):
        common_dfs.append(df)
    else:
        not_common_dfs.append(df)
        
if common_dfs:
    merged_df = common_dfs[0]

    for df in common_dfs[1:]:
        merged_df = pd.merge(merged_df, df, on=['Entity', 'Year'], how='outer')

        if 'Code_x' in merged_df.columns and 'Code_y' in merged_df.columns:
            merged_df['FINAL_CODE'] = merged_df['Code_x'].fillna(merged_df['Code_y'])
            merged_df = merged_df.drop(columns=['Code_x', 'Code_y'])
            merged_df.rename(columns={'FINAL_CODE': 'Code'}, inplace=True)
            

merged_df_post_1970 = merged_df[merged_df['Year'] >= 1970]

#Dataframe Cleaning

from fuzzywuzzy import process

# Function to find closest match for NaN rows
def fill_continent_with_closest_match(entity, entity_to_continent):

    closest_match = process.extractOne(entity, entity_to_continent.keys())
    if closest_match and closest_match[1] > 80:  
        return entity_to_continent[closest_match[0]]
    else:
        return None
    
entity_to_continent = {
    'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa', 'Andorra': 'Europe', 
    'Angola': 'Africa', 'Argentina': 'South America', 'Armenia': 'Asia', 'Australia': 'Oceania', 
    'Austria': 'Europe', 'Azerbaijan': 'Asia', 'Bahamas': 'North America', 'Bahrain': 'Asia',
    'Bangladesh': 'Asia', 'Barbados': 'North America', 'Belarus': 'Europe', 'Belgium': 'Europe',
    'Belize': 'North America', 'Benin': 'Africa', 'Bhutan': 'Asia', 'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe', 'Botswana': 'Africa', 'Brazil': 'South America', 'Brunei': 'Asia',
    'Bulgaria': 'Europe', 'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cabo Verde': 'Africa',
    'Cambodia': 'Asia', 'Cameroon': 'Africa', 'Canada': 'North America', 'Central African Republic': 'Africa',
    'Chad': 'Africa', 'Chile': 'South America', 'China': 'Asia', 'Colombia': 'South America',
    'Comoros': 'Africa', 'Congo': 'Africa', 'Costa Rica': 'North America', 'Croatia': 'Europe',
    'Cuba': 'North America', 'Cyprus': 'Asia', 'Czech Republic': 'Europe', 'Denmark': 'Europe',
    'Djibouti': 'Africa', 'Dominica': 'North America', 'Dominican Republic': 'North America', 'Ecuador': 'South America',
    'Egypt': 'Africa', 'El Salvador': 'North America', 'Equatorial Guinea': 'Africa', 'Eritrea': 'Africa',
    'Estonia': 'Europe', 'Eswatini': 'Africa', 'Ethiopia': 'Africa', 'Fiji': 'Oceania',
    'Finland': 'Europe', 'France': 'Europe', 'Gabon': 'Africa', 'Gambia': 'Africa', 'Georgia': 'Asia',
    'Germany': 'Europe', 'Ghana': 'Africa', 'Greece': 'Europe', 'Grenada': 'North America', 'Guatemala': 'North America',
    'Guinea': 'Africa', 'Guinea-Bissau': 'Africa', 'Guyana': 'South America', 'Haiti': 'North America',
    'Honduras': 'North America', 'Hungary': 'Europe', 'Iceland': 'Europe', 'India': 'Asia', 'Indonesia': 'Asia',
    'Iran': 'Asia', 'Iraq': 'Asia', 'Ireland': 'Europe', 'Israel': 'Asia', 'Italy': 'Europe',
    'Jamaica': 'North America', 'Japan': 'Asia', 'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa',
    'Kiribati': 'Oceania', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Latvia': 'Europe',
    'Lebanon': 'Asia', 'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa', 'Liechtenstein': 'Europe',
    'Lithuania': 'Europe', 'Luxembourg': 'Europe', 'Madagascar': 'Africa', 'Malawi': 'Africa', 'Malaysia': 'Asia',
    'Maldives': 'Asia', 'Mali': 'Africa', 'Malta': 'Europe', 'Marshall Islands': 'Oceania', 'Mauritania': 'Africa',
    'Mauritius': 'Africa', 'Mexico': 'North America', 'Micronesia': 'Oceania', 'Moldova': 'Europe', 'Monaco': 'Europe',
    'Mongolia': 'Asia', 'Montenegro': 'Europe', 'Morocco': 'Africa', 'Mozambique': 'Africa', 'Myanmar': 'Asia',
    'Namibia': 'Africa', 'Nauru': 'Oceania', 'Nepal': 'Asia', 'Netherlands': 'Europe', 'New Zealand': 'Oceania',
    'Nicaragua': 'North America', 'Niger': 'Africa', 'Nigeria': 'Africa', 'North Korea': 'Asia', 'North Macedonia': 'Europe',
    'Norway': 'Europe', 'Oman': 'Asia', 'Pakistan': 'Asia', 'Palau': 'Oceania', 'Panama': 'North America',
    'Papua New Guinea': 'Oceania', 'Paraguay': 'South America', 'Peru': 'South America', 'Philippines': 'Asia',
    'Poland': 'Europe', 'Portugal': 'Europe', 'Qatar': 'Asia', 'Romania': 'Europe', 'Russia': 'Europe',
    'Rwanda': 'Africa', 'Saint Kitts and Nevis': 'North America', 'Saint Lucia': 'North America',
    'Saint Vincent and the Grenadines': 'North America', 'Samoa': 'Oceania', 'San Marino': 'Europe',
    'Sao Tome and Principe': 'Africa', 'Saudi Arabia': 'Asia', 'Senegal': 'Africa', 'Serbia': 'Europe',
    'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Singapore': 'Asia', 'Slovakia': 'Europe', 'Slovenia': 'Europe',
    'Solomon Islands': 'Oceania', 'Somalia': 'Africa', 'South Africa': 'Africa', 'South Korea': 'Asia',
    'South Sudan': 'Africa', 'Spain': 'Europe', 'Sri Lanka': 'Asia', 'Sudan': 'Africa', 'Suriname': 'South America',
    'Sweden': 'Europe', 'Switzerland': 'Europe', 'Syria': 'Asia', 'Taiwan': 'Asia', 'Tajikistan': 'Asia',
    'Tanzania': 'Africa', 'Thailand': 'Asia', 'Togo': 'Africa', 'Tonga': 'Oceania', 'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 'Tuvalu': 'Oceania', 'Uganda': 'Africa',
    'Ukraine': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe', 'United States': 'North America',
    'Uruguay': 'South America', 'Uzbekistan': 'Asia', 'Vanuatu': 'Oceania', 'Venezuela': 'South America',
    'Vietnam': 'Asia', 'Yemen': 'Asia', 'Zambia': 'Africa', 'Zimbabwe': 'Africa'
}

# Drop the old Continent columns
df_cleaned = merged_df_post_1970.drop(columns=['Continent_x', 'Continent_y'])

df_cleaned['Continent'] = df_cleaned['Entity'].map(entity_to_continent)

entities_with_nan = df_cleaned[df_cleaned['Continent'].isna()]['Entity'].unique()

closest_matches = {}
for entity in entities_with_nan:
    closest_match = process.extractOne(entity, entity_to_continent.keys())
    if closest_match and closest_match[1] > 80:  
        closest_matches[entity] = entity_to_continent[closest_match[0]]
    else:
        closest_matches[entity] = None
        
df_cleaned['Continent'] = df_cleaned.apply(
    lambda row: closest_matches.get(row['Entity'], row['Continent']) if pd.isna(row['Continent']) else row['Continent'],axis=1)

df_cleaned = df_cleaned.dropna(subset=['Continent'])


drop_list = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica', 'Latin America and Caribbean']

df_cleaned = df_cleaned[~df_cleaned['Entity'].str.contains(r'\b(?:' + '|'.join(drop_list) + r')\b', case=False, na=False)]


### FILLING IN MISSING MIN CALORIE DATA BASED ON MEDIAN VALUE BY YEAR OF CLOSEST NEIGHBORS ### 
neighbors = {
    'Afghanistan': ['Pakistan', 'Iran', 'Turkmenistan', 'Uzbekistan', 'Tajikistan', 'China'],
    'Albania': ['Montenegro', 'Kosovo', 'North Macedonia', 'Greece'], 
    'Algeria': ['Tunisia', 'Libya', 'Niger', 'Mali', 'Mauritania', 'Morocco'],
    'Angola': ['Namibia', 'Zambia', 'Democratic Republic of the Congo'],
    'Argentina': ['Chile', 'Bolivia', 'Paraguay', 'Brazil', 'Uruguay'],
    'Armenia': ['Georgia', 'Turkey', 'Iran', 'Azerbaijan'],
    'Australia': ['Papua New Guinea', 'New Zealand', 'Indonesia'],  
    'Austria': ['Germany', 'Czech Republic', 'Slovakia', 'Hungary', 'Slovenia', 'Italy', 'Switzerland'],
    'Azerbaijan': ['Russia', 'Georgia', 'Armenia', 'Iran'],
    'Bahamas': ['United States', 'Cuba', 'Haiti'],  
    'Bahrain': ['Saudi Arabia', 'Qatar'],  
    'Bangladesh': ['India', 'Myanmar'],
    'Barbados': ['Saint Lucia', 'Saint Vincent and the Grenadines', 'Grenada'],  
    'Belgium': ['Netherlands', 'Germany', 'Luxembourg', 'France'],
    'Belize': ['Mexico', 'Guatemala'],
    'Benin': ['Togo', 'Burkina Faso', 'Niger', 'Nigeria'],
    'Bhutan': ['India', 'China'],
    'Bolivia': ['Peru', 'Brazil', 'Paraguay', 'Argentina', 'Chile'],
    'Bosnia and Herzegovina': ['Croatia', 'Serbia', 'Montenegro'],
    'Botswana': ['Namibia', 'Zimbabwe', 'Zambia', 'South Africa'],
    'Brazil': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    'Brunei': ['Malaysia', 'Indonesia'],  
    'Bulgaria': ['Romania', 'Serbia', 'North Macedonia', 'Greece', 'Turkey'],
    'Burkina Faso': ['Mali', 'Niger', 'Benin', 'Togo', 'Ghana', 'Cote d’Ivoire'],
    'Burundi': ['Rwanda', 'Tanzania', 'Democratic Republic of the Congo'],
    'Cambodia': ['Thailand', 'Vietnam', 'Laos'],
    'Cameroon': ['Nigeria', 'Chad', 'Central African Republic', 'Equatorial Guinea', 'Gabon', 'Republic of the Congo'],
    'Canada': ['United States'],
    'Cape Verde': ['Senegal', 'Gambia'],  
    'Central African Republic': ['Chad', 'Sudan', 'South Sudan', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Cameroon'],
    'Chad': ['Libya', 'Sudan', 'Central African Republic', 'Cameroon', 'Nigeria', 'Niger'],
    'Chile': ['Peru', 'Bolivia', 'Argentina'],
    'China': ['India', 'Russia', 'Mongolia', 'Kazakhstan', 'North Korea', 'Nepal', 'Bhutan', 'Pakistan', 'Afghanistan', 'Vietnam', 'Laos', 'Myanmar'],
    'Colombia': ['Venezuela', 'Brazil', 'Peru', 'Ecuador', 'Panama'],
    'Comoros': ['Madagascar', 'Mozambique'],  
    'Congo': ['Gabon', 'Cameroon', 'Central African Republic', 'Democratic Republic of the Congo', 'Angola'],
    'Costa Rica': ['Nicaragua', 'Panama'],
    'Cote d’Ivoire': ['Liberia', 'Guinea', 'Mali', 'Burkina Faso', 'Ghana'],
    'Croatia': ['Slovenia', 'Hungary', 'Serbia', 'Bosnia and Herzegovina', 'Montenegro'],
    'Cuba': ['United States', 'Mexico', 'Haiti', 'Jamaica'],  
    'Cyprus': ['Turkey', 'Syria', 'Lebanon'],  
    'Czech Republic': ['Germany', 'Poland', 'Slovakia', 'Austria'],
    'Denmark': ['Germany', 'Sweden', 'Norway'],  
    'Djibouti': ['Eritrea', 'Ethiopia', 'Somalia'],
    'Dominica': ['Guadeloupe', 'Martinique', 'Saint Lucia'], 
    'Dominican Republic': ['Haiti', 'Puerto Rico'],  
    'Ecuador': ['Colombia', 'Peru'],
    'Egypt': ['Libya', 'Sudan', 'Israel'],
    'El Salvador': ['Guatemala', 'Honduras'],
    'Equatorial Guinea': ['Gabon', 'Cameroon', 'Sao Tome and Principe'],  
    'Eritrea': ['Sudan', 'Ethiopia', 'Djibouti'],
    'Estonia': ['Russia', 'Latvia'],
    'Eswatini': ['Mozambique', 'South Africa'],
    'Ethiopia': ['Eritrea', 'Djibouti', 'Somalia', 'Kenya', 'South Sudan', 'Sudan'],
    'Fiji': ['Tonga', 'Vanuatu', 'New Caledonia'],  
    'Finland': ['Sweden', 'Norway', 'Russia'],
    'France': ['Belgium', 'Luxembourg', 'Germany', 'Switzerland', 'Italy', 'Monaco', 'Spain', 'Andorra'],
    'Gabon': ['Equatorial Guinea', 'Cameroon', 'Republic of the Congo'],
    'Gambia': ['Senegal'],
    'Georgia': ['Russia', 'Azerbaijan', 'Armenia', 'Turkey'],
    'Germany': ['Denmark', 'Poland', 'Czech Republic', 'Austria', 'Switzerland', 'France', 'Luxembourg', 'Belgium', 'Netherlands'],
    'Ghana': ['Cote d’Ivoire', 'Burkina Faso', 'Togo'],
    'Greece': ['Albania', 'North Macedonia', 'Bulgaria', 'Turkey'],
    'Grenada': ['Saint Vincent and the Grenadines', 'Trinidad and Tobago'],  
    'Guatemala': ['Mexico', 'Belize', 'Honduras', 'El Salvador'],
    'Guinea': ['Guinea-Bissau', 'Senegal', 'Mali', 'Cote d’Ivoire', 'Liberia', 'Sierra Leone'],
    'Guinea-Bissau': ['Senegal', 'Guinea'],
    'Guyana': ['Venezuela', 'Brazil', 'Suriname'],
    'Haiti': ['Dominican Republic', 'Cuba'],  
    'Honduras': ['Guatemala', 'El Salvador', 'Nicaragua'],
    'Hungary': ['Austria', 'Slovakia', 'Ukraine', 'Romania', 'Serbia', 'Croatia', 'Slovenia'],
    'Iceland': ['Greenland', 'Norway', 'United Kingdom'],  
    'India': ['Pakistan', 'China', 'Nepal', 'Bhutan', 'Bangladesh', 'Myanmar'],
    'Indonesia': ['Malaysia', 'Papua New Guinea', 'East Timor'],  
    'Iran': ['Pakistan', 'Afghanistan', 'Turkmenistan', 'Azerbaijan', 'Armenia', 'Turkey', 'Iraq'],
    'Iraq': ['Turkey', 'Iran', 'Kuwait', 'Saudi Arabia', 'Jordan', 'Syria'],
    'Ireland': ['United Kingdom'],  
    'Israel': ['Lebanon', 'Syria', 'Jordan', 'Egypt'],
    'Italy': ['France', 'Switzerland', 'Austria', 'Slovenia'],
    'Jamaica': ['Cuba', 'Haiti', 'Dominican Republic'],  
    'Japan': ['South Korea', 'China', 'Russia'],  
    'Jordan': ['Syria', 'Iraq', 'Saudi Arabia', 'Israel'],
    'Kazakhstan': ['Russia', 'China', 'Kyrgyzstan', 'Uzbekistan', 'Turkmenistan'],
    'Kenya': ['Somalia', 'Ethiopia', 'South Sudan', 'Uganda', 'Tanzania'],
    'Kiribati': ['Marshall Islands', 'Tuvalu'],  
    'Kuwait': ['Iraq', 'Saudi Arabia'],
    'Kyrgyzstan': ['Kazakhstan', 'Uzbekistan'],
    'Laos': ['China', 'Vietnam', 'Cambodia', 'Thailand', 'Myanmar'],
    'Latvia': ['Estonia', 'Russia', 'Belarus', 'Lithuania'],
    'Lebanon': ['Syria', 'Israel'],
    'Lesotho': ['South Africa'],
    'Liberia': ['Sierra Leone', 'Guinea', 'Cote d’Ivoire'],
    'Libya': ['Tunisia', 'Algeria', 'Niger', 'Chad', 'Sudan', 'Egypt'],
    'Liechtenstein': ['Switzerland', 'Austria'],
    'Lithuania': ['Latvia', 'Belarus', 'Poland', 'Russia'],
    'Luxembourg': ['Belgium', 'France', 'Germany'],
    'Madagascar': ['Mozambique', 'Comoros'], 
    'Malawi': ['Tanzania', 'Mozambique', 'Zambia'],
    'Malaysia': ['Thailand', 'Indonesia', 'Brunei', 'Singapore'],
    'Maldives': ['Sri Lanka', 'India'], 
    'Mali': ['Algeria', 'Niger', 'Burkina Faso', 'Cote d’Ivoire', 'Guinea', 'Mauritania', 'Senegal'],
    'Malta': ['Italy', 'Tunisia'],  
    'Marshall Islands': ['Micronesia', 'Kiribati'],  
    'Mauritania': ['Morocco', 'Western Sahara', 'Algeria', 'Mali', 'Senegal'],
    'Mauritius': ['Madagascar', 'Reunion'],  
    'Mexico': ['United States', 'Guatemala', 'Belize'],
    'Micronesia': ['Marshall Islands', 'Palau'],  
    'Moldova': ['Romania', 'Ukraine'],
    'Monaco': ['France'],  
    'Mongolia': ['Russia', 'China'],
    'Montenegro': ['Bosnia and Herzegovina', 'Serbia', 'Kosovo', 'Albania', 'Croatia'],
    'Morocco': ['Algeria', 'Western Sahara', 'Spain (Ceuta and Melilla)'],  
    'Mozambique': ['Tanzania', 'Malawi', 'Zambia', 'Zimbabwe', 'South Africa', 'Eswatini'],
    'Myanmar': ['China', 'Laos', 'Thailand', 'Bangladesh', 'India'],
    'Namibia': ['Angola', 'Zambia', 'Botswana', 'South Africa'],
    'Nauru': ['Kiribati', 'Marshall Islands'],  
    'Nepal': ['China', 'India'],
    'Netherlands': ['Germany', 'Belgium'],
    'New Zealand': ['Australia', 'Fiji', 'Tonga'],  
    'Nicaragua': ['Honduras', 'Costa Rica'],
    'Niger': ['Libya', 'Chad', 'Nigeria', 'Benin', 'Burkina Faso', 'Mali', 'Algeria'],
    'Nigeria': ['Niger', 'Benin', 'Cameroon', 'Chad'],
    'North Korea': ['China', 'South Korea', 'Russia'],
    'North Macedonia': ['Kosovo', 'Serbia', 'Bulgaria', 'Greece', 'Albania'],
    'Norway': ['Sweden', 'Finland', 'Russia'],
    'Oman': ['United Arab Emirates', 'Saudi Arabia', 'Yemen'],
    'Pakistan': ['Afghanistan', 'China', 'India', 'Iran'],
    'Palau': ['Philippines', 'Micronesia'],  
    'Panama': ['Costa Rica', 'Colombia'],
    'Papua New Guinea': ['Indonesia', 'Solomon Islands', 'Australia'],  
    'Paraguay': ['Brazil', 'Argentina', 'Bolivia'],
    'Peru': ['Ecuador', 'Colombia', 'Brazil', 'Bolivia', 'Chile'],
    'Philippines': ['Malaysia', 'Taiwan', 'Brunei', 'Indonesia'],  
    'Poland': ['Germany', 'Czech Republic', 'Slovakia', 'Ukraine', 'Belarus', 'Lithuania', 'Russia'],
    'Portugal': ['Spain'],
    'Qatar': ['Saudi Arabia', 'United Arab Emirates'],  
    'Romania': ['Ukraine', 'Moldova', 'Bulgaria', 'Serbia', 'Hungary'],
    'Russia': ['Norway', 'Finland', 'Estonia', 'Latvia', 'Lithuania', 'Poland', 'Belarus', 'Ukraine', 'Georgia', 'Azerbaijan', 'Kazakhstan', 'China', 'Mongolia', 'North Korea'],
    'Rwanda': ['Uganda', 'Tanzania', 'Burundi', 'Democratic Republic of the Congo'],
    'Saint Kitts and Nevis': ['Antigua and Barbuda', 'Saint Barthelemy', 'Saint Martin'],  
    'Saint Lucia': ['Barbados', 'Saint Vincent and the Grenadines'],  
    'Saint Vincent and the Grenadines': ['Saint Lucia', 'Barbados', 'Grenada'],  
    'Samoa': ['American Samoa', 'Tonga', 'Fiji'],  
    'San Marino': ['Italy'],  
    'Sao Tome and Principe': ['Gabon', 'Equatorial Guinea'],  
    'Saudi Arabia': ['Jordan', 'Iraq', 'Kuwait', 'Bahrain', 'Qatar', 'United Arab Emirates', 'Oman', 'Yemen'],
    'Senegal': ['Mauritania', 'Mali', 'Guinea', 'Guinea-Bissau', 'Gambia'],
    'Serbia': ['Bosnia and Herzegovina', 'Montenegro', 'Kosovo', 'Macedonia', 'Bulgaria', 'Romania', 'Hungary', 'Croatia'],
    'Seychelles': ['Mauritius', 'Madagascar'],  
    'Sierra Leone': ['Guinea', 'Liberia'],
    'Singapore': ['Malaysia', 'Indonesia'],  
    'Slovakia': ['Czech Republic', 'Austria', 'Hungary', 'Ukraine', 'Poland'],
    'Slovenia': ['Italy', 'Austria', 'Hungary', 'Croatia'],
    'Solomon Islands': ['Papua New Guinea', 'Vanuatu'],  
    'Somalia': ['Ethiopia', 'Djibouti', 'Kenya'],
    'South Africa': ['Namibia', 'Botswana', 'Zimbabwe', 'Mozambique', 'Eswatini', 'Lesotho'],
    'South Korea': ['North Korea', 'China', 'Japan'],  
    'South Sudan': ['Sudan', 'Ethiopia', 'Kenya', 'Uganda', 'Democratic Republic of the Congo', 'Central African Republic'],
    'Spain': ['Portugal', 'France', 'Andorra', 'Gibraltar'],  
    'Sri Lanka': ['India', 'Maldives'],  
    'Sudan': ['Egypt', 'Libya', 'Chad', 'Central African Republic', 'South Sudan', 'Eritrea', 'Ethiopia'],
    'Suriname': ['Guyana', 'Brazil', 'French Guiana'],
    'Sweden': ['Norway', 'Finland'],
    'Switzerland': ['France', 'Germany', 'Austria', 'Italy'],
    'Syria': ['Turkey', 'Iraq', 'Jordan', 'Israel', 'Lebanon'],
    'Taiwan': ['China', 'Japan', 'Philippines'],  
    'Tajikistan': ['Afghanistan', 'Uzbekistan', 'Kyrgyzstan', 'China'],
    'Tanzania': ['Kenya', 'Uganda', 'Rwanda', 'Burundi', 'Democratic Republic of the Congo', 'Zambia', 'Malawi', 'Mozambique'],
    'Thailand': ['Myanmar', 'Laos', 'Cambodia', 'Malaysia'],
    'Timor-Leste': ['Indonesia', 'Australia'],  
    'Togo': ['Ghana', 'Burkina Faso', 'Benin'],
    'Tonga': ['Fiji', 'Samoa'],  
    'Trinidad and Tobago': ['Grenada', 'Venezuela'],  
    'Tunisia': ['Algeria', 'Libya'],               
    'Turkey': ['Greece', 'Bulgaria', 'Georgia', 'Armenia', 'Azerbaijan', 'Iran', 'Iraq', 'Syria'],
    'Turkmenistan': ['Kazakhstan', 'Uzbekistan', 'Afghanistan', 'Iran'],
    'Tuvalu': ['Kiribati', 'Fiji', 'Samoa'],  
    'Uganda': ['Kenya', 'South Sudan', 'Democratic Republic of the Congo', 'Rwanda', 'Tanzania'],
    'Ukraine': ['Poland', 'Slovakia', 'Hungary', 'Romania', 'Moldova', 'Belarus', 'Russia'],
    'United Arab Emirates': ['Oman', 'Saudi Arabia'],
    'United Kingdom': ['Ireland', 'France', 'Belgium', 'Netherlands'],  
    'United States': ['Canada', 'Mexico'],
    'Uruguay': ['Argentina', 'Brazil'],
    'Uzbekistan': ['Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Afghanistan', 'Turkmenistan'],
    'Vanuatu': ['Fiji', 'Solomon Islands', 'New Caledonia'],  
    'Vatican City': ['Italy'],  
    'Venezuela': ['Colombia', 'Brazil', 'Guyana'],
    'Vietnam': ['China', 'Laos', 'Cambodia'],
    'Yemen': ['Saudi Arabia', 'Oman'],
    'Zambia': ['Angola', 'Democratic Republic of the Congo', 'Tanzania', 'Malawi', 'Mozambique', 'Zimbabwe', 'Botswana', 'Namibia'],
    'Zimbabwe': ['Zambia', 'Mozambique', 'South Africa', 'Botswana']}

# Function to compute the median for neighboring countries or fall back to overall median

df_cleaned.rename(columns={df_cleaned.columns[6]: 'MIN_DIET_ENERGY_REQ'}, inplace=True)
df_cleaned.rename(columns={df_cleaned.columns[3]: 'GDP_PER_CAP'}, inplace=True)
df_cleaned.rename(columns={df_cleaned.columns[4]: 'POP'}, inplace=True)

df_cleaned['MIN_DIET_ENERGY_REQ'] = df_cleaned['MIN_DIET_ENERGY_REQ'].replace(['nan', 'NaN', 'None', ''], pd.NA)
df_cleaned['MIN_DIET_ENERGY_REQ'] = pd.to_numeric(df_cleaned['MIN_DIET_ENERGY_REQ'], errors='coerce')

def fill_min_dietary_energy(row, column_name, df, neighbors_dict):
    country = row['Entity']
    year = row['Year']
    continent = row['Continent']  # Assuming there is a 'Continent' column

    if country in neighbors_dict:
        neighbor_countries = neighbors_dict[country]
        neighbor_values = df[(df['Entity'].isin(neighbor_countries)) & (df['Year'] == year)][column_name].dropna()
        
        if len(neighbor_values) > 0:
            print(f"Using neighbor median for {country}, {year}")
            return neighbor_values.median()

    continent_values = df[(df['Continent'] == continent) & (df['Year'] == year)][column_name].dropna()
    if len(continent_values) > 0:
        print(f"Using continent median for {continent}, {year}")
        return continent_values.median()

    available_years = df[(df['Entity'] == country) & (~df[column_name].isna())]['Year'].unique()
    if len(available_years) > 0:
        closest_year = min(available_years, key=lambda x: abs(x - year))
        closest_year_median = df[(df['Entity'] == country) & (df['Year'] == closest_year)][column_name].median()
        print(f"Using closest year ({closest_year}) median for {country}")
        return closest_year_median

    available_continent_years = df[(df['Continent'] == continent) & (~df[column_name].isna())]['Year'].unique()
    if len(available_continent_years) > 0:
        closest_year = min(available_continent_years, key=lambda x: abs(x - year))
        closest_continent_year_median = df[(df['Continent'] == continent) & (df['Year'] == closest_year)][column_name].median()
        print(f"Using closest year ({closest_year}) median for {continent}")
        return closest_continent_year_median

    global_median = df[column_name].median()
    print("Using global fallback median")
    return global_median

df_cleaned['MIN_DIET_ENERGY_REQ'] = df_cleaned.apply(
    lambda row: fill_min_dietary_energy(row, 'MIN_DIET_ENERGY_REQ', df_cleaned, neighbors) 
    if pd.isna(row['MIN_DIET_ENERGY_REQ']) 
    else row['MIN_DIET_ENERGY_REQ'],
    axis=1
)


### FILL IN GDP DATA FOR ALL COUNTRIES USING WORLDBANK API ###
import wbdata as wb
import datetime

gdp_data = wb.get_dataframe(
    {"NY.GDP.MKTP.CD": "GDP"})

gdp_data.reset_index(inplace=True)

gdp_data.dropna(inplace=True)

gdp_data = gdp_data[gdp_data.loc[:,'date'].between('1970', '2023')]
gdp_data['date'] = gdp_data['date'].astype(int)


# Step 3: Merge on fuzzy-matched Entity and exact Year
gdp_merged_df = pd.merge(df_cleaned, gdp_data, left_on=['Entity', 'Year'], right_on=['country', 'date'], how='left')

# Function to fill the GDP_PER_CAP column
def fill_GDP_PER_CAP(df):

    for i, row in df.iterrows():
        if not pd.isna(row['GDP']) and not pd.isna(row['POP']):  # Check if both GDP and POP are not NaN
            df.at[i, 'GDP_PER_CAP'] = row['GDP'] / row['POP']  # Fill with GDP / POP
    return df


gdp_merged_df_adj = fill_GDP_PER_CAP(gdp_merged_df)


### FILL IN MALNUTRITION DATASET WITH DATA 2000 -> PRESENT ###

file_path = 'C:/Users/Musuki/OneDrive - UW/Desktop/CS3112_PROJECTFILE/API_SN.ITK.DEFC.ZS_DS2_en_csv_v2_10009.csv'
df = pd.read_csv(file_path)
df_long = df.melt(id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
                  var_name="Year", value_name="Value")

df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')
df_long_clean = df_long.dropna(subset=['Value'])

malnut_merged_df = pd.merge(gdp_merged_df_adj, df_long_clean, left_on=['Code', 'Year'], right_on=['Country Code', 'Year'], how='left')
malnut_merged_df = malnut_merged_df.drop(columns=["country", "date","Country Name", "Country Code", "Indicator Name", "Indicator Code"])
malnut_merged_df.rename(columns={malnut_merged_df.columns[-1]: '% TOTAL POP MALNURISH'}, inplace=True)


### ADD UNDER 5 CHILD MORTALITY RATE ### 

file_path = 'C:/Users/Musuki/OneDrive - UW/Desktop/CS3287_PROJECT/Under-five_Mortality_Rates_2023.xlsx'
df_mortality = pd.read_excel(file_path)
df_mortality_long = df_mortality.melt(id_vars=["ISOCode", "CountryName"], var_name="Year", value_name="MortalityRate")
df_mortality_long['Year'] = pd.to_numeric(df_mortality_long['Year'], errors='coerce')
df_mortality_long_clean = df_mortality_long.dropna(subset=['MortalityRate'])

mortality_df_clean = pd.merge(malnut_merged_df, df_mortality_long_clean, left_on=['Code', 'Year'], right_on=['ISOCode', 'Year'], how='left')
mortality_df_clean = mortality_df_clean.drop(columns=["ISOCode", "CountryName","GDP per capita, PPP (constant 2017 international $)_y"])
mortality_df_clean.rename(columns={mortality_df_clean.columns[-1]: 'MORTALITY_PER_1000_BIRTHS'}, inplace=True)

def fill_earliest_non_null(data):
   
    for col in data.columns:
        first_non_null_index = data[col].first_valid_index()
        
        if first_non_null_index is not None:
            first_non_null_value = data[col][first_non_null_index]
            data[col] = data[col].fillna(method='ffill').fillna(first_non_null_value)
    
    return data

final_df = fill_earliest_non_null(mortality_df_clean)
final_df.columns
final_df.drop('2.1.1 Prevalence of undernourishment | 000000000024000 || Value | 006121 || Percent', axis=1, inplace=True)
final_df.rename(columns={
                    'Entity':'entity','Year':'year','GDP_PER_CAP':'gdp_per_cap','POP':'pop','MIN_DIET_ENERGY_REQ':'min_diet_energy_req','Code':'code',
                    'Continent':'continent','MORTALITY_PER_1000_BIRTHS':'mortality_per_1000_births',
                   '2.1.1 Number of undernourished people | 000000000024001 || Value | 006132 || million Number': 'millions_undernourished_people',
                   'Prevalence of underweight, weight for age (% of children under 5)': 'percent_children_under_5_underweight',
                   'Prevalence of wasting, weight for height (% of children under 5)':'percent_children_under_5_wasting',
                    'Share of children who are stunted':'percent_children_stunted',
                     'Prevalence of moderate or severe food insecurity in the total population (percent) (3-year average) | 00210091 || Value | 006121 || Percent':'percent_of_total_pop_suffering_moderate_food_insecurity'
                     }, 
                    inplace=True)

old_name = final_df.columns[2]
new_name = 'coefficient_of_variation_of_caloric_intake'
final_df.rename(columns={old_name: new_name}, inplace=True)

old_name = final_df.columns[5]
new_name = 'total_deaths_from_protein_energy_malnutrition_among_both_sexes'
final_df.rename(columns={old_name: new_name}, inplace=True)

old_name = final_df.columns[-2]
new_name = 'percent_total_pop_malnurish'
final_df.rename(columns={old_name: new_name}, inplace=True)

old_name = final_df.columns[-3]
new_name = 'gdp'
final_df.rename(columns={old_name: new_name}, inplace=True)


    
final_df= final_df.rename(columns=str.lower)
final_df['unique_id'] = range(1, len(final_df) + 1)
final_df.columns = final_df.columns.str.lower()
final_df.columns
final_df.dtypes

### CREATE TABLE AND INSERT DATA ###


import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='global_hunger_project')


cursor = conn.cursor()



create_table_query = """ CREATE TABLE IF NOT EXISTS global_hunger_project.starvation_source_table (
    unique_id INT AUTO_INCREMENT PRIMARY KEY,
    entity VARCHAR(50),
    year VARCHAR(50),
    coefficient_of_variation_of_caloric_intake DOUBLE,
    gdp_per_cap DOUBLE,
    pop DOUBLE,
    total_deaths_from_protein_energy_malnutrition_among_both_sexes DOUBLE,
    min_diet_energy_req DOUBLE,
    millions_undernourished_people DOUBLE,
    percent_children_under_5_underweight DOUBLE,
    percent_children_under_5_wasting DOUBLE,
    percent_children_stunted DOUBLE,
    percent_of_total_pop_suffering_moderate_food_insecurity DOUBLE,
    code VARCHAR(50),
    continent VARCHAR(50),
    gdp DOUBLE,
    percent_total_pop_malnurish DOUBLE,
    mortality_per_1000_births DOUBLE );""" 


cursor.execute(create_table_query)
conn.commit()
final_df.columns 

for index, row in final_df.iterrows():
    sql_query = """
                       INSERT INTO global_hunger_project.starvation_source_table (entity,year, 
                       coefficient_of_variation_of_caloric_intake,gdp_per_cap,pop,
                       total_deaths_from_protein_energy_malnutrition_among_both_sexes,
                       min_diet_energy_req,millions_undernourished_people,
                       percent_children_under_5_underweight,percent_children_under_5_wasting,
                       percent_children_stunted,percent_of_total_pop_suffering_moderate_food_insecurity,
                       code,continent,gdp,percent_total_pop_malnurish, mortality_per_1000_births)
                       VALUES (
                           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    values = (
            str(row['entity']),
            int(row['year']),
            float(row['coefficient_of_variation_of_caloric_intake']),
            float(row['gdp_per_cap']),
            float(row['pop']),
            float(row['total_deaths_from_protein_energy_malnutrition_among_both_sexes']),
            float(row['min_diet_energy_req']),
            float(row['millions_undernourished_people']),
            float(row['percent_children_under_5_underweight']),
            float(row['percent_children_under_5_wasting']),
            float(row['percent_children_stunted']),
            float(row['percent_of_total_pop_suffering_moderate_food_insecurity']),
            str(row['code']),
            str(row['continent']),
            float(row['gdp']),
            float(row['percent_total_pop_malnurish']),
            float(row['mortality_per_1000_births'])
            )
    
    print(f"Executing SQL: {sql_query} with values: {values}")

    cursor.execute(sql_query,values)
    conn.commit()



crop_df = pd.read_csv(r'C:\Users\Musuki\OneDrive - UW\Desktop\CS3287_PROJECT\crop1.csv', encoding = 'utf-8')
crop_df.columns = crop_df.columns.str.strip()
crop_df.dropna(subset=['Value'], inplace = True)

cursor = conn.cursor()

create_table_query = """ CREATE TABLE IF NOT EXISTS global_hunger_project.crop_data 
    (
     Area VARCHAR(250),
     Item VARCHAR(250),
     Element VARCHAR(250),
     Year INT,
     Unit VARCHAR(250),
     Value FLOAT
     )
     """
cursor.execute(create_table_query)

# Insert data into the table
for index, row in crop_df.iterrows():
    insert_query = """
    INSERT INTO global_hunger_project.crop_data  (Area, Item, Element, Year, Unit, Value)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    crop_values = (row['Area'], row['Item'], row['Element'], row['Year'], row['Unit'], row['Value'])
    
    cursor.execute(insert_query,crop_values)

# Commit the changes
conn.commit()


# Close the connection
cursor.close()
conn.close()






