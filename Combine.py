
import pandas as pd
import glob
import os

### choose only LAC from US News
# df = pd.read_csv('/Users/ada1024/Desktop/Ranking/US News LAC - Cleaned LAC ranking (1).csv')
# filtered_df = df[df['US_institution.schoolType'] == 'national-liberal-arts-colleges']
# filtered_df.to_csv('/Users/ada1024/Desktop/Ranking/US News LAC.csv', index=False)

# Adjust the pattern to look for CSV files in the 'rank_with_state' subdirectory
csv_files = glob.glob('rank_with_state/*.csv')
print(f"Found {len(csv_files)} CSV files.")

# Initialize an empty DataFrame
merged_df = pd.DataFrame(columns=['Name', 'state'])

# Loop through the long establiashed CSV files and merge them based on name and state
for file in csv_files:
    try:
        # Read the CSV file
        df = pd.read_csv(file, on_bad_lines='skip')  # Skip bad lines
        # Print column names for debugging
        print(f"Columns in {file}: {df.columns.tolist()}")

        # Check for 'Name' column
        if 'Name' not in df.columns:
            raise KeyError(f"'Name' column is missing in {file}")

        # Check for 'state' column
        if 'state' not in df.columns:
            raise KeyError(f"'state' column is missing in {file}")

        # Normalize the 'Name' and 'state' columns
        df['Name'] = df['Name'].str.strip().str.lower()
        df['state'] = df['state'].str.strip().str.lower()

        # Merge DataFrames; for the first merge, if merged_df is empty, simply assign df
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=['Name', 'state'], how='outer')

    except pd.errors.ParserError as e:
        print(f"Error parsing {file}: {e}")
    except KeyError as e:
        print(e)

for additional_file in ['new_rankings/dc_lac.csv', 'new_rankings/ai_lac.csv']:
    try:
        df_additional = pd.read_csv(additional_file)
        
        # Print column names for debugging
        print(f"Columns in {additional_file}: {df_additional.columns.tolist()}")

        # Check for 'Name' column
        if 'Name' not in df_additional.columns:
            raise KeyError(f"'Name' column is missing in {additional_file}")

        # Normalize the 'Name' column
        df_additional['Name'] = df_additional['Name'].str.strip().str.lower()

        # Perform outer merge with merged_df
        merged_df = pd.merge(merged_df, df_additional, on='Name', how='outer')

    except pd.errors.ParserError as e:
        print(f"Error parsing {additional_file}: {e}")
    except KeyError as e:
        print(e)

# Save the final merged DataFrame to a new CSV file
output_file = 'final_merged_rankings.csv'
merged_df.to_csv(output_file, index=False)
print(f"Final merged DataFrame saved to {output_file}")





