import sys
import gzip
import zipfile
import os
import re

# Define fixed paths
LOG_ZIP_PATH = "logs_2024.log.zip"  # Change this to the actual ZIP file path
OUTPUT_DIR = "output"  # Directory to save extracted logs

def extract_logs(target_date):
    try:
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        output_file_path = os.path.join(OUTPUT_DIR, f"output_{target_date}.txt")
        
        # Check if the file is a valid ZIP archive
        if not os.path.exists(LOG_ZIP_PATH):
            print("Error: ZIP file not found.")
            return
        if not zipfile.is_zipfile(LOG_ZIP_PATH):
            print("Error: The specified file is not a valid ZIP archive.")
            return
        
        date_pattern = re.compile(rf'^{re.escape(target_date)}')  # Match lines that start with the target date
        
        with zipfile.ZipFile(LOG_ZIP_PATH, 'r') as zip_ref, open(output_file_path, 'w', encoding='utf-8') as output_file:
            for file_name in zip_ref.namelist():
                if file_name.endswith('.log') or file_name.endswith('.gz'):
                    with zip_ref.open(file_name) as log_file:
                        open_func = gzip.open if file_name.endswith('.gz') else lambda f: f
                        with open_func(log_file) as log_data:
                            for line in log_data:
                                decoded_line = line.decode('utf-8', errors='ignore')
                                if date_pattern.match(decoded_line):
                                    output_file.write(decoded_line)
        
        print(f"Filtered log entries saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <target_date>")
    else:
        extract_logs(sys.argv[1])
