# Import necessary library
import pandas as pd

# Define file paths for reading and writing Excel files
read_file_path = "file_path"
write_file_path = "file_path"

# Load the Excel file into pandas DataFrames for two sheets
df_main = pd.read_excel(read_file_path)
df_sheet2 = pd.read_excel(read_file_path, sheet_name='Sheet2')

# Define the LogP range for classification
MIN_LOGP = 4.9
MAX_LOGP = 23

# Initialize a list to keep track of classes found within the specified LogP range
classes_found = []

def find_index(value):
    """Determine the index based on the 'Number of C' value."""
    # Define the range as tuples of (lower_bound, upper_bound, index)
    ranges = [(i*5, (i+1)*5, i) for i in range(12)]
    # Return the corresponding index for the value
    for lower, upper, index in ranges:
        if lower <= value < upper:
            return index
    return 11  # Default to 11 if no range matches

# Iterate through each row in the DataFrame
for index, row in df_main.iterrows():
    logp = row["LogP"]
    # Check if the LogP value falls within the specified range
    if MIN_LOGP < logp < MAX_LOGP:
        classe = row["Class"]
        # Add unique classes to the list
        if classe not in classes_found:
            classes_found.append(classe)
            c = row["Number of C"]
            row_index = find_index(c)
            data = row["fatty acyls"]
            # Update the second DataFrame with the found data
            df_sheet2.loc[row_index, classe] = data

# Display the updated DataFrame
print(df_sheet2)

# Save the modified DataFrame back to an Excel file, preserving modifications
df_sheet2.to_excel(write_file_path, sheet_name="Sheet2", index=False)
