import os
import random

# Especifica la ruta de la carpeta
folder_path = './dataset/tristeza'

# Lista todos los archivos en la carpeta
files = os.listdir(folder_path)

# Filtra para obtener solo archivos (excluye directorios)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Calcula cuántos archivos eliminar (la mitad)
num_files_to_delete = len(files) // 2

# Selecciona aleatoriamente los archivos a eliminar
files_to_delete = random.sample(files, num_files_to_delete)

# Elimina los archivos seleccionados
for file in files_to_delete:
    file_path = os.path.join(folder_path, file)
    os.remove(file_path)
    print(f'Eliminado: {file_path}')
