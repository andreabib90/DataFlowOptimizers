import pandas as pd

# Define the path to the CSV file containing the merged names
file_path = 'file_name'

def extract_filename(file_path):
    """
    Extract specific parts of the filename based on its structure.
    
    Parameters:
    - file_path: The full path or name of the file.
    
    Returns:
    A tuple containing the extracted parts of the filename or (None, None) if the criteria are not met.
    """
    # Split the filename by underscores to isolate components
    parts = file_path.split('_')
    
    # Ensure there are enough parts to extract the desired segments
    if len(parts) >= 9:
        # Concatenate and return the specified parts
        extracted_name1 = '_'.join(parts[2:4])
        extracted_name2 = '_'.join(parts[7:9])
        return extracted_name1, extracted_name2
    else:
        return None, None

# Load the CSV data into a DataFrame
df = pd.read_csv(file_path)

# Apply the filename extraction function to each entry in the 'Meged Name' column
# and split the results into two new columns
df[['Extracted_Name_1', 'Extracted_Name_2']] = df['Meged Name'].apply(
    lambda x: extract_filename(x)).tolist()

# Save the DataFrame with the new columns back to a CSV file
df.to_csv('file_name', index=False)
