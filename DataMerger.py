import pandas as pd
import os

# Import data from the first CSV file
file1_path = 'file_path'
df1 = pd.read_csv(file1_path)

# Import data from the second CSV file
file2_path = 'file_path'  # Replace with the actual path to the second file
df2 = pd.read_csv(file2_path)

# Find the common column names between the two DataFrames
common_columns = df1.columns.intersection(df2.columns)

# Keep only the common columns in both DataFrames
df1 = df1[common_columns]
df2 = df2[common_columns]

# Combine the two dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

combined_df.to_csv('file_path', index=False)