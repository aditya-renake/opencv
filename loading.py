import cv2
image = cv2.imread("avr.jpeg")

if image is None:
    print("Error image not found") 

else:
    print("Image loaded succesfully ")


#image = cv2.imread("imagename.jpg", flag)
