import difflib
import os

def compare_python_files(file1_path, file2_path):
    """Compare two Python files and print differences."""
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        diff = difflib.unified_diff(lines1, lines2, lineterm="")
        diff_text = "\n".join(diff)

        if diff_text:
            print(f"Differences in file: {file1_path}")
            print(diff_text)
            print("#" * 125)

def compare_python_directories(directory1, directory2):
    """Compare Python files in two directories."""
    # Walk through the first directory
    for root, _, files in os.walk(directory1):
        for filename in files:
            if filename.endswith(".py"):
                file1_path = os.path.join(root, filename)
                file2_path = os.path.join(directory2, file1_path[len(directory1) + 1:])

                # Check if corresponding file exists in the second directory
                if os.path.exists(file2_path):
                    try:
                        compare_python_files(file1_path, file2_path)
                    except Exception as e:
                        print(f"Error comparing files: {e}")

# Main function to compare directories
def main():
    directory1 = 'directory'
    directory2 = 'directory'
    compare_python_directories(directory1, directory2)
    print('Done')

if __name__ == "__main__":
    main()
