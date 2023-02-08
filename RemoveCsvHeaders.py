# ! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current

import csv, os

os.makedirs("headerRemoved", exist_ok=True)

# Loop through every file in the current working directory
for csv_file in os.listdir("."):
    if not csv_file.endswith(".csv"):
        continue

    print("removing header from " + csv_file + "...")

    # Read the CSV file in (skipping first row)
    csvRows = []
    csv_file_obj = open(csv_file)
    csv_file_reader = csv.reader(csv_file_obj)
    for row in csv_file_reader:
        if csv_file_reader.line_num == 1:
            continue  # skip first row
        csvRows.append(row)
    csv_file_obj.close()

    # Write out CSV file.
    csv_file_obj = open(os.path.join("headerRemoved", csv_file), "w", newline="")
    csv_writer = csv.writer(csv_file_obj)
    for row in csvRows:
        csv_writer.writerow(row)
    csv_file_obj.close()