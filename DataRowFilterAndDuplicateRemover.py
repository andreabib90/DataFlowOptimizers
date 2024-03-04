import pandas as pd
import os

# Import data from the merged CSV file
file1_path = 'file_path'
df = pd.read_csv(file1_path)

# Find and keep rows with the highest 'Average1' value for each duplicate 'Metabolite name'
df = df.sort_values(by=['Metabolite name', 'Average1'], ascending=[True, False])
df = df.drop_duplicates(subset='Metabolite name', keep='first')

# Compare and remove rows based on "Average MZ" and "Average Rt(min)" columns
rows_to_remove = []
count = 1

for index, row in df.iterrows():
    current_name = row['Metabolite name']  # Get the current Metabolite name
    current_rt = row['Average Rt(min)']
    # Define the interval boundaries
    lower_bound = current_rt - 0.15
    upper_bound = current_rt + 0.15
    current_mz = row['Average Mz']
    current_average = row['Average1']

    for _, other_row in df.iterrows():
        if index != _:
            other_name=other_row['Metabolite name']
            #if current_name == other_name: #only apply filter if IDs are the same
            if other_row['Average Rt(min)'] >= lower_bound and other_row['Average Rt(min)'] <= upper_bound:
                if abs(current_mz - other_row['Average Mz']) < 0.005:
                    if current_average < other_row['Average1']:
                        if index not in rows_to_remove:
                                rows_to_remove.append(index)
                    else:
                        if _ not in rows_to_remove:
                            rows_to_remove.append(_)
    count += 1
    if count % 200 == 0:
        print(f"Row: {count}")
        print(f"Number of rows to remove so far: {len(rows_to_remove)}")


# Save the dataframe with Fraction information
#df.to_csv('F5/F5_MergedFinal_2.csv', index=False)
# Remove duplicate rows
filtered_csv = df.drop(rows_to_remove)

filtered_csv.to_csv('file_path', index=False)
