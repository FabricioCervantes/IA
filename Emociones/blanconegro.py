from PIL import Image
import os

# Especifica la ruta de la carpeta
folder_path = './dataset/tristeza'

# Lista todos los archivos en la carpeta
files = os.listdir(folder_path)

# Filtra para obtener solo archivos de imagen (puedes ajustar las extensiones según tus necesidades)
image_files = [f for f in files if f.lower().endswith(
    ('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

# Convierte cada imagen a blanco y negro
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    # Abre la imagen
    with Image.open(image_path) as img:
        # Convierte la imagen a blanco y negro
        bw_img = img.convert('L')
        # Guarda la imagen convertida (puedes sobrescribir la original o guardar en una nueva carpeta)
        bw_img.save(image_path)
        print(f'Convertido a blanco y negro: {image_path}')
