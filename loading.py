import cv2
image = cv2.imread("avr.jpeg")

if image is None:
    print("Error imagge not found")

else:
    print("Image loaded succesfully")
