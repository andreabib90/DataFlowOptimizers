import os
import csv

# Define the path to the directory you want to traverse
directory_path = "path"

# Initialize a dictionary to store filenames organized by their directory
files_dict = {}

def extract_filename(file_path):
    """
    Extract specific parts of the filename based on underscores.
    
    Args:
    - file_path: The path of the file from which to extract parts of the filename.
    
    Returns:
    - extracted_name1: A string containing the extracted part of the filename.
    """
    # Split the filename by underscores
    parts = file_path.split('_')
    
    # Join the desired parts of the filename
    extracted_name1 = '_'.join(parts[2:4])
    return extracted_name1

def traverse_directory(directory):
    """
    Traverse through the given directory and subdirectories to extract and store filenames.
    
    Args:
    - directory: The root directory to start the traversal.
    """
    for root, dirs, files in os.walk(directory):
        current_files = [extract_filename(file) for file in files if '_' in file]
        files_dict[root] = current_files

# Traverse the specified directory
traverse_directory(directory_path)

# Define the filename for the output CSV
csv_filename = 'path_file'

# Write the dictionary data to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for key, values in files_dict.items():
        for value in values:
            csv_writer.writerow([key, value])
