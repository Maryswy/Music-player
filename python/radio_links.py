import os
import csv
from tqdm import tqdm  # Import the tqdm library for progress bar

# Create a list to store extracted data
data = []

# Define the directory path
root_dir = "/home/mostafa/Desktop/projects/Music-player/m3u-radio-music-playlists"

# Get the total number of .m3u files for progress tracking
total_files = sum(1 for root, dirs, files in os.walk(root_dir) for file in files if file.endswith(".m3u"))

# Traverse the directory structure to find .m3u files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".m3u"):
            file_path = os.path.join(dirpath, filename)
            
            # Read content of the .m3u file
            with open(file_path, "r") as file:
                content = file.read()
            
            # Extract relevant information
            file_info = {
                "Filename": filename,
                "Path": file_path,
                "Content": content
            }
            
            # Append extracted information to the data list
            data.append(file_info)
            
            # Update progress bar
            with tqdm(total=total_files, desc="Processing") as pbar:
                pbar.update(1)

# Write extracted information to a CSV file
csv_file = "radio_info.csv"
csv_columns = ["Filename", "Path", "Content"]

with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print("CSV file created successfully!")

