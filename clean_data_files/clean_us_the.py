import pandas as pd

def clean_fil(input_filename, output_filename):
    # Read the CSV file
    df = pd.read_csv(input_filename)
    
    # Clean the 'Name' column by removing text within parentheses and trimming whitespace
    df['Name'] = df['Name'].str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip()
    
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_filename, index=False)
    
    print(f"Cleaned data saved to {output_filename}")

# Example usage
clean_fil('us_lac.csv', 'modified_us_lac.csv')
clean_fil('the_lac.csv', 'modified_the_lac.csv')

