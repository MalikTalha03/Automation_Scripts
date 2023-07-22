import os
from PIL import Image

def resize_images(input_folder, output_folder, target_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        # Check if the file is an image (ending with common image file extensions)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # Open the image
            image = Image.open(input_path)

            # Calculate the new dimensions while preserving the aspect ratio
            width, height = image.size
            if width > height:
                new_width = target_size
                new_height = int(height * (target_size / width))
            else:
                new_width = int(width * (target_size / height))
                new_height = target_size

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            # Save the resized image to the output folder
            resized_image.save(output_path)

# Set the input and output folder paths and the target size (3072 x 3072)
input_folder = str(input("Enter Source path: "))
output_folder = str(input("Enter Destination path: "))
target_size = int(input("Enter desired dimension of image (for 2074 x 2074 enter 2074): "))

# Call the function to resize images
resize_images(input_folder, output_folder, target_size)
