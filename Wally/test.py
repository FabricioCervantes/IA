import cv2
import os

cascade_path = 'data2/cascade.xml'
wally_cascade = cv2.CascadeClassifier(cascade_path)

window_name = 'Detections'


def detect_wally(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error al cargar la imagen {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    wally = wally_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(24, 24)
    )

    for (x, y, w, h) in wally:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    cv2.imshow(window_name, image)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return True
    cv2.destroyAllWindows()
    return False


def detect_wally_in_folder(folder_path):
    image_files = [f for f in os.listdir(
        folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"Detecting Wally in {image_path}")
        if detect_wally(image_path):
            print("Cancelando el proceso.")
            break


def evaluate_on_folder(folder_path):
    image_files = [f for f in os.listdir(
        folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        if detect_wally(image_path):
            print("Cancelando el proceso.")
            break


# test_folder = 'test'
# detect_wally_in_folder(test_folder)

# validation_folder = 'valid'
# evaluate_on_folder(validation_folder)

final_folder = 'original-images'
evaluate_on_folder(final_folder)
