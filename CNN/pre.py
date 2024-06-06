import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

print("Comenzando el preprocesamiento de datos...")

# Ruta a los datasets
dataset_path = 'dataset'  # Ajusta esta ruta a donde tengas tu dataset

# Tamaño de las imágenes
IMG_SIZE = 128

# Función para cargar y procesar las imágenes


def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            images.append(img)
            labels.append(label)
    return images, labels


# Carga de imágenes para cada categoría
categories = ['asalto', 'robo_casa', 'tornado', 'inundacion', 'incendio']
all_images = []
all_labels = []

print("Cargando imágenes...")

for idx, category in enumerate(categories):
    folder_path = os.path.join(dataset_path, category)
    images, labels = load_images_from_folder(folder_path, idx)
    all_images.extend(images)
    all_labels.extend(labels)
    print(f"Categoría '{category}' cargada con {len(images)} imágenes.")

# Convertir a numpy arrays
X = np.array(all_images)
y = np.array(all_labels)

print("Normalizando imágenes...")

# Normalizar imágenes
X = X / 255.0

print("Dividiendo el dataset en conjuntos de entrenamiento, validación y prueba...")

# Dividir en conjuntos de entrenamiento, validación y prueba
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.1765, random_state=42)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de validación: {len(X_val)}")
print(f"Datos de prueba: {len(X_test)}")

print("Configurando el aumento de datos...")

# Aumento de datos
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

datagen.fit(X_train)

print("Construyendo el modelo CNN...")

# Definir la arquitectura de la CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(categories), activation='softmax')  # 5 clases de peligro
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print("Entrenando el modelo...")

# Entrenamiento del modelo con aumento de datos
history = model.fit(datagen.flow(X_train, y_train, batch_size=32),
                    epochs=25, validation_data=(X_val, y_val))

print("Evaluando el modelo...")

# Evaluación del modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {test_acc}")
