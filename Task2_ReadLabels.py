import cv2
import numpy as np
from glob import glob

# Load the list of image file paths in your folder
image_paths = glob('Chess Pieces.v24-416x416_aug.yolov5pytorch/train/images/*.jpg')

# Load the saved coordinates from the text files
corner_coordinates_list = []
for i, image_path in enumerate(image_paths):
    txt_filename = f"coordinates_image_{image_path.split('/')[-1]}.txt"
    
    with open(txt_filename, "r") as txt_file:
        coordinates = [tuple(map(int, line.strip().split(','))) for line in txt_file]
    
    corner_coordinates_list.append(coordinates)

print(coordinates)
# Show the saved coordinates on the images
for i, image_path in enumerate(image_paths):
    img = cv2.imread(image_path)
    coordinates = corner_coordinates_list[i]
    
    for (x, y) in coordinates:
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    cv2.imshow(f"Image {i + 1} with Coordinates", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
