import pandas as pd

# Read the CSV file
df = pd.read_csv('file_path')

# Define sample groups
sample_groups = {
    'Group 1': ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4'],
    'Group 1': ['Sample 5', 'Sample 6', 'Sample 7', 'Sample 8'],
    'Group 1': ['Sample 9', 'Sample 10', 'Sample 11', 'Sample 12'],
    # Add more groups if needed
}

# Specify the threshold percentage for each group
threshold_percentage = 0.75  # Example: 75%

# Filter out rows with 'ID' column containing 'Unknown'
df = df[df['Metabolite name'] != 'Unknown']

# Filter out rows where SN ratio is below 3
df = df[df['S/N average'] > 3]

# Filter out rows where any average column is equal to zero
average_columns = ['Average1', 'Average2', 'Average3']
for col in average_columns:
    df = df[df[col] != 0]

# Filter out rows where average column is smaller than corresponding StDev column
for i in range(1, 4):
    df = df[df[f'Average{i}'] > df[f'Stdev{i}']]

# Define an empty list to store conditions
conditions = []

# Generate conditions for each sample group
for group_name, group_columns in sample_groups.items():
    group_data = df[group_columns]
    num_columns = len(group_columns)
    condition = (group_data.eq(0).sum(axis=1) / num_columns) <= threshold_percentage
    conditions.append(condition)

# Combine conditions for all groups using logical AND
final_condition = conditions[0]
for condition in conditions[1:]:
    final_condition = final_condition & condition

# Apply the final condition to filter the DataFrame
df = df[final_condition]

# Save the filtered DataFrame
df.to_csv('file_path', index=False)
