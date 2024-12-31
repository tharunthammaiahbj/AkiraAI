import os
import shutil
import random

# Path to the folder containing the files
source_folder = '/workspaces/AkiraAI/Dataset/Summarization/input_markdown'

# Path to the destination folder where shuffled files will be saved
destination_folder = '/workspaces/AkiraAI/Dataset/Summarization/mixed_input_markdown'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Get a list of all the files in the source folder
all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Count the number of files
num_files = len(all_files)

# Print the number of files
print(f"Number of files in source folder: {num_files}")

# Shuffle the list of files randomly
random.shuffle(all_files)

# Copy the shuffled files to the destination folder with new names
for i, file_name in enumerate(all_files):
    src_path = os.path.join(source_folder, file_name)
    dest_path = os.path.join(destination_folder, f"page_{i+1}.md")
    shutil.copy(src_path, dest_path)

print(f"Successfully shuffled {num_files} files and saved to {destination_folder}")
