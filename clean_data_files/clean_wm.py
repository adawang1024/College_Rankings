import pandas as pd
import re

# Load the dataset
df = pd.read_csv('wm_lac.csv') 
def extract_state(name):
    match = re.search(r'\((.*?)\)', name)  # Search for content inside parentheses
    return match.group(1) if match else None  # Return the content, or None if no match

# Create a new column 'state' with the extracted content
df['state'] = df['Name'].apply(extract_state)
df['Name'] = df['Name'].str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip()


# Optionally, save the modified dataframe to a new CSV file
df.to_csv('modified_wm.csv', index=False)