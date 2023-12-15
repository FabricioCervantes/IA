```
from PIL import Image
import os
import cv2

# Directories
input_dir = './datasets/A'
intermediate_dirs = {
    'squared': './datasets/Squared',
    'filtered': './datasets/Filtered',
    'rotated': './datasets/Rotated'
}
output_name = 'tulip'

# Create intermediate directories
for dir_path in intermediate_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# Standardize size
target_size = (128, 128)
input_files = os.listdir(input_dir)
for input_file in input_files:
    process_image_standardize_size(input_dir, intermediate_dirs['squared'], input_file, target_size)

# Apply filters
input_files = os.listdir(intermediate_dirs['squared'])
for input_file in input_files:
    process_image_apply_filters(intermediate_dirs['squared'], intermediate_dirs['filtered'], input_file)

# Rotate images
input_files = os.listdir(intermediate_dirs['filtered'])
for input_file in input_files:
    process_image_rotate(intermediate_dirs['filtered'], intermediate_dirs['rotated'], input_file, target_size)

# Rename images
rename_images(intermediate_dirs['rotated'], output_name)

print("Image processing complete.")


def process_image_standardize_size(input_dir, output_dir, input_file, target_size):
    input_path = os.path.join(input_dir, input_file)
    output_path = os.path.join(output_dir, input_file)
    
    img = Image.open(input_path)
    width, height = img.size
    size = min(width, height)
    
    # Calculate coordinates for the square crop
    left = (width - size) / 2
    upper = (height - size) / 2
    right = (width + size) / 2
    lower = (height + size) / 2
    
    square_img = img.crop((left, upper, right, lower))
    square_img.thumbnail(target_size)
    small_img = Image.new('RGB', target_size, (255, 255, 255))
    offset = ((target_size[0] - square_img.width) // 2, (target_size[1] - square_img.height) // 2)
    small_img.paste(square_img, offset)
    small_img.save(output_path)


def process_image_apply_filters(input_dir, output_dir, input_file):
    input_path = os.path.join(input_dir, input_file)
    output_path_original = os.path.join(output_dir, input_file)

    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error processing {input_file}: {str(e)}")
        return

    filename, _ = os.path.splitext(input_file)
    img.save(output_path_original)

    grayscale_img = img.convert('L')
    grayscale_filename = f"{filename}_grayscale"
    grayscale_img.save(os.path.join(output_dir, f"{grayscale_filename}.jpg"))

    img_array = cv2.imread(input_path)
    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2HSV)
    hsv_img = Image.fromarray(hsv_img)
    hsv_filename = f"{filename}_hsv"
    hsv_img.save(os.path.join(output_dir, f"{hsv_filename}.jpg"))


def process_image_rotate(input_dir, output_dir, input_file, target_size):
    input_path = os.path.join(input_dir, input_file)
    
    img = Image.open(input_path)
    for i in range(0, 360, 15):
        rotated_img = img.rotate(i, expand=True)

        if i not in (0, 90, 180, 270):
            width, height = rotated_img.size
            new_width = new_height = min(width, height) // 2
            left = (width - new_width) // 2
            upper = (height - new_height) // 2
            right = left + new_width
            lower = upper + new_height
            rotated_img = rotated_img.crop((left, upper, right, lower))
            rotated_img = rotated_img.resize(target_size)

        output_filename = f"rotated_{i}_degrees_{input_file}"
        output_path = os.path.join(output_dir, output_filename)
        rotated_img.save(output_path)
```