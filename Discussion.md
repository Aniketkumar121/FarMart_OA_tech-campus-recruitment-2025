Solutions Considered
We explored a couple of different ways to tackle this problem:
Extracting the ZIP file first and then processing logs
This approach would involve extracting all files from logs.zip into a temporary directory and filtering the logs from there.
❌ Issue: Since the ZIP file is 700MB+, extracting everything would take a lot of disk space (especially on limited storage).
Reading the ZIP file directly without extraction (Final Approach)
Instead of extracting everything, we open the ZIP file and process logs line by line.
✅ Advantages:
Saves disk space (no full extraction needed).
It is faster because we avoid unnecessary I/O operations.
Memory-efficient since we only keep relevant log lines instead of loading the entire file into memory.
This was the best approach given the constraints!
Final Solution Summary
We chose the second approach because it avoids unnecessary disk writes, optimizes memory usage, and directly processes logs inside the ZIP.
The script reads each file from the ZIP, checks if it's a .log or .gz file, and then streams lines instead of extracting them.
Only lines that start with the given data are written to the output file.
Supports both plain .log files and compressed .gz logs dynamically.
Steps to Run the Script
Ensure you have Python installed.
Run the python --version to confirm.
Place your ZIP file in the correct directory:
logs.zip should be in large_logs/
Run the script with a specific date:
		python extract_logs.py 2024-12-01
Find the filtered logs in the output/ directory:
Example: output/output_2024-12-01.txt will contain all log entries from December 1, 2024.
