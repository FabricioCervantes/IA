import os
import glob
import xml.etree.ElementTree as ET


def parse_xml_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = []
    for member in root.findall('object'):
        bbox = member.find('bndbox')
        bbox_data = {
            'xmin': int(bbox.find('xmin').text),
            'ymin': int(bbox.find('ymin').text),
            'xmax': int(bbox.find('xmax').text),
            'ymax': int(bbox.find('ymax').text)
        }
        objects.append(bbox_data)
    return objects


def create_positives_txt(image_folder, output_file):
    with open(output_file, 'w') as f:
        for xml_file in glob.glob(os.path.join(image_folder, '*.xml')):
            image_file = xml_file.replace('.xml', '.jpg')
            if os.path.exists(image_file):
                objects = parse_xml_annotation(xml_file)
                for obj in objects:
                    line = f"{image_file} 1 {obj['xmin']} {obj['ymin']} {obj['xmax'] - obj['xmin']} {obj['ymax'] - obj['ymin']}\n"
                    f.write(line)
    print(f"Successfully created {output_file}")


image_folder = 'train'
output_file = 'positives.txt'
create_positives_txt(image_folder, output_file)
