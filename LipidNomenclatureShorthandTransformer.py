import pandas as pd
import re

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('file_path')

def process_metabolite_name(metabolite_name):
    """
    Process the metabolite name to extract and format its shorthand notation.
    """
    prefix = metabolite_name.split()[0]
    after_first_space = ' '.join(metabolite_name.split()[1:])
    suffix = "".join(re.findall(r'\([^)]+\)', after_first_space))
    after_first_space = re.sub(r'\([^)]*\)', "", after_first_space)

    # Handling the second prefix, assuming 'O-' is a marker for it
    second_prefix = "O-" if not after_first_space[0].isnumeric() else ""
    
    # Summation of numbers before and after the colon
    sum_of_numbers = sum(map(int, re.findall(r'(\d+):', after_first_space)))
    sum_of_second_numbers = sum(map(int, re.findall(r':(\d+)', after_first_space)))

    # Count 'O's in the string, excluding those part of a chemical notation like O2
    o_count = sum(map(len, re.findall(r"O(?!\d)", after_first_space)))
    for i in range(2, 6):
        if f"O{i}" in after_first_space:
            o_count += i

    final_o = "O" if o_count == 1 else f"O{o_count}" if o_count > 1 else ""
    
    # Final formatting
    final_suffix = ";" + suffix if suffix and not suffix.startswith("(FA") else suffix
    base_result = f"{prefix} {second_prefix}{sum_of_numbers}:{sum_of_second_numbers}"
    result = f"{base_result};{final_o}{final_suffix}" if o_count or final_suffix else base_result

    return result

# Apply processing to each row and update the DataFrame
df['Shorthand notation'] = df['Metabolite name'].apply(process_metabolite_name)

# Save the updated DataFrame to a new CSV file
df.to_csv('file_path', index=False)
