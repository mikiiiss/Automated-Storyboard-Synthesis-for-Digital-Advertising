import os
import shutil

# Define the path to the main asset folder and the destination folder
asset_folder = 'Data/w12data/Archive/Challenge_Data/Challenge_Data/Assets'
destination_folder = 'asset'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through each subfolder in the main asset folder
for subdir in os.listdir(asset_folder):
    subdir_path = os.path.join(asset_folder, subdir)
    
    # Check if it is a directory
    if os.path.isdir(subdir_path):
        endframe_path = os.path.join(subdir_path, 'endframe.jpg')
        preview_path = os.path.join(subdir_path, '_preview.png')
        
        # Check if the endframe.jpg exists in the current subdirectory
        if os.path.exists(endframe_path):
            # Create a unique name for each endframe.jpg based on the parent folder name
            endframe_destination_file = os.path.join(destination_folder, f"{subdir}_endframe.jpg")
            # Copy the endframe.jpg to the destination folder with the new name
            shutil.copy(endframe_path, endframe_destination_file)
        
        # Check if the _preview.png exists in the current subdirectory
        if os.path.exists(preview_path):
            # Create a unique name for each _preview.png based on the parent folder name
            preview_destination_file = os.path.join(destination_folder, f"{subdir}_preview.png")
            # Copy the _preview.png to the destination folder with the new name
            shutil.copy(preview_path, preview_destination_file)

print("All endframe.jpg and _preview.png files have been copied to the destination folder.")