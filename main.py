import os
from PIL import Image

# Define the input/output folder
input_folder = r"C:\GitHub\compressor\src\in"
output_folder = r"C:\GitHub\compressor\src\out"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop over all files in the input folder
for i, filename in enumerate(os.listdir(input_folder)):
    # Only process .jpg files
    if filename.lower().endswith(".jpg"):
        # Construct full file path
        file_path = os.path.join(input_folder, filename)

        # Open and compress the image
        with Image.open(file_path) as img:
            # Save the compressed image with a new name starting from 0.jpg
            output_path = os.path.join(output_folder, f"{i}.jpg")
            img.save(output_path, "JPEG", quality=75, optimize=True)

print(f"All images have been compressed and saved to {output_folder}")
