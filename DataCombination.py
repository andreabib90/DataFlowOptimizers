import pandas as pd
import os

# Import data from the first CSV file
file1_path = 'file_path_1'
df1 = pd.read_csv(file1_path)
df1['Fraction'] = '1'

# Import data from the second CSV file
file2_path = 'file_path_2'
df2 = pd.read_csv(file2_path)
df2['Fraction'] = '2'

# Import data from the third CSV file
file3_path = 'file_path_3'
df3 = pd.read_csv(file3_path)
df3['Fraction'] = '3'

# Import data from the fourth CSV file
file4_path = 'file_path_4'
df4 = pd.read_csv(file4_path)
df4['Fraction'] = '4'

# Import data from the fifth CSV file
file5_path = 'file_path_5'
df5 = pd.read_csv(file5_path)
df5['Fraction'] = '5'

# Combine all dataframes into a single dataframe
combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Save the combined dataframe with Fraction information
combined_df.to_csv('file_name', index=False)
