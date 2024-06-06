import os
import cv2


def validate_coordinates(image_folder, positives_file, output_file):
    valid_lines = []
    with open(positives_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            image_path = os.path.join(image_folder, parts[0])
            if os.path.exists(image_path):
                image = cv2.imread(image_path)
                height, width = image.shape[:2]

                xmin = int(parts[2])
                ymin = int(parts[3])
                xmax = xmin + int(parts[4])
                ymax = ymin + int(parts[5])

                if 0 <= xmin < width and 0 <= ymin < height and 0 < xmax <= width and 0 < ymax <= height:
                    valid_lines.append(line.strip())
                else:
                    print(
                        f"Invalid coordinates for {image_path}: {xmin}, {ymin}, {xmax}, {ymax}")
            else:
                print(f"Image {image_path} not found.")

    with open(output_file, 'w') as file:
        for line in valid_lines:
            file.write(line + '\n')

    print(f"Validation completed. Valid entries are saved to {output_file}")


image_folder = ''
positives_file = 'positives.txt'
output_file = 'positives_valid.txt'

validate_coordinates(image_folder, positives_file, output_file)
