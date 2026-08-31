import cv2
image = cv2.imread("avr.jpeg")

if image is not None:
    cv2.imshow("Image Showing", image) #open the window
    cv2.waitKey(0) #wait for a key
    cv2.destroyAllWindows() #closes all the windows
    print("Error imagge not found") #close the window

else:
    print("Could not load the image")


#image = cv2.imread("imagename.jpg", flag)
