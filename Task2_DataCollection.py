import cv2
import numpy as np
from glob import glob

# Create a list to store the corner coordinates for each image
corner_coordinates_list = []

# Load the list of image file paths in your folder
image_paths = glob('Chess Pieces.v24-416x416_aug.yolov5pytorch/train/images/*.jpg')


# Define a callback function for mouse click events
def mouse_callback(event, x, y, flags, param):
    global corner_coordinates

    # If left mouse button is clicked, save the coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        # Append the clicked coordinates to the list
        corner_coordinates.append((x, y))
        # Draw a point where the user clicked
        cv2.circle(img_copy, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Chessboard", img_copy)

        # If we have collected all four corners, save them and clear the list
        if len(corner_coordinates) == 5:
            corner_coordinates_list.append(corner_coordinates.copy())
            corner_coordinates.clear()

# Loop through each image in the folder
for image_path in image_paths[:3]:
    # Load the image
    img = cv2.imread(image_path)
    img_copy = img.copy()
    
    # Create a window and set the mouse callback function
    cv2.imshow("Chessboard", img_copy)
    corner_coordinates = [image_path.split('/')[-1]]

    # Wait for the user to manually select the four corners
    cv2.setMouseCallback("Chessboard", mouse_callback)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Write the collected corner coordinates to a text file for each image
for i, coordinates in enumerate(corner_coordinates_list):
    txt_filename = f"coordinates_image_{coordinates[0]}.txt"
    coordinates.pop(0)
    with open(txt_filename, "w") as txt_file:
        for (x, y) in coordinates:
            txt_file.write(f"{x}, {y}\n")

    print(f"Coordinates for Image {i + 1} saved to {txt_filename}")
