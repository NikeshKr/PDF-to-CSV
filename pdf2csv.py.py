#!/usr/bin/env python
# coding: utf-8

# In[16]:


import tabula
import pandas as pd

# Provide the path to your PDF file
pdf_file = "enter pdf name"

# Provide the path to save the CSV file
csv_output = "nsut_output.csv"

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate through each page of the PDF
for page in range(1, 117):
    # Read the table from the current page
    df = tabula.read_pdf(pdf_file, pages=page, pandas_options={"header": None})
    
    # Remove the header row from the table
    df = df[1:]
    
    # Concatenate the current page's data to the combined data
    combined_data = pd.concat([combined_data, df])

# Reset the index of the combined data
combined_data.reset_index(drop=True, inplace=True)

# Save the combined data as a CSV file
combined_data.to_csv(csv_output, index=False)

# Remove missing values
combined_data.dropna(inplace=True)

# Perform data profiling
from pandas_profiling import ProfileReport

profile = ProfileReport(combined_data, title="Data Profiling Report")

# Save the report as an HTML file
profile.to_file("data_profiling_report.html")


# In[ ]:


import tabula
import pandas as pd

# Provide the path to your PDF file
pdf_file = "Gazette Report B Tech 6th Sem 2022-23.pdf"

# Provide the path to save the CSV file
csv_output = "nsut_output.csv"

# Create an empty list to store the individual DataFrames
df_list = []

# Iterate through each page of the PDF
for page in range(1, 117):
    # Read the table from the current page
    df = tabula.read_pdf(pdf_file, pages=page, pandas_options={"header": None})
    
    # Remove the header row from the table
    df = df[1:]
    
    # Append the current page's DataFrame to the list
    df_list.append(df)

# Concatenate all the DataFrames in the list
combined_data = pd.concat(df_list, ignore_index=True)

# Save the combined data as a CSV file
combined_data.to_csv(csv_output, index=False)

# Remove missing values
combined_data.dropna(inplace=True)

# Perform data profiling
from pandas_profiling import ProfileReport

profile = ProfileReport(combined_data, title="Data Profiling Report")

# Save the report as an HTML file
profile.to_file("data_profiling_report.html")

