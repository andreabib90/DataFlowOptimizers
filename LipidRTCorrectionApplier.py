import pandas as pd

# Define file paths for input and output Excel files
lipid_classes_path = "file_path"
subclass_timegroup_path = "file_path"
output_path = "output_file_path"

# Load the Excel files into DataFrames
df_lipid_classes = pd.read_excel(lipid_classes_path)
df_subclass_to_timegroup = pd.read_excel(subclass_timegroup_path)

# Initialize a dictionary to map lipid abbreviations to their respective time groups
time_groups = {}

# Populate the time_groups dictionary from the DataFrame
for index, row in df_subclass_to_timegroup.iterrows():
    time_groups[row["Abbreviation"]] = (
        row["Time group <14C"], row["Time group 14-20C"], row["Time group 21-33C"],
        row["Time group 34-45C"], row["Time group >45C"]
    )

def get_sum_of_numbers(string):
    """Calculate the sum of numbers in a string, separated by semicolons."""
    parts = string.split(';')
    total_sum = 0
    for part in parts:
        number = ''.join(filter(str.isdigit, part))
        total_sum += int(number) if number else 1  # Count non-numbers as 1
    return total_sum

def find_carbon_index(value):
    """Determine the carbon group index based on the number of carbons."""
    if value < 10:
        return 0
    elif value < 20:
        return 1
    elif value < 30:
        return 2
    elif value < 40:
        return 3
    else:
        return 4

def find_adjustment(value):
    """Map the value to a specific adjustment factor."""
    return 0.00 if value == 0 else value * 0.01

def calculate_penalties(tg, db, mods):
    """Calculate the final time group with penalties for double bonds and modifications."""
    tg_final = tg - db - mods
    return round(tg_final)

# Update the DataFrame with corrected time groups
for index, row in df_lipid_classes.iterrows():
    classe = row["Lipid class"]
    carbon = row["#C"]
    db = row["DB"]
    mods = row["Modifications"]
    
    carbon_index = find_carbon_index(carbon)
    time_group = time_groups[classe][carbon_index]
    
    db_adjustment = find_adjustment(db)
    mods_sum = get_sum_of_numbers(str(mods))
    mods_adjustment = find_adjustment(mods_sum)

    tg_final = calculate_penalties(time_group, db_adjustment, mods_adjustment)

    df_lipid_classes.at[index, "Time group"] = tg_final

# Save the modified DataFrame to an Excel file
df_lipid_classes.to_excel(output_path, index=False)
