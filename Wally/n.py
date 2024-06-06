import os


def create_negatives_txt(negatives_folder, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(negatives_folder):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    f.write(os.path.join(root, file) + '\n')
    print(f"Successfully created {output_file}")


negatives_folder = 'negatives'
output_file = 'negatives.txt'

create_negatives_txt(negatives_folder, output_file)
