import cv2

image = cv2.imread("Phase 2(Image Drawing Functions)/avr.jpeg")
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    pt1 = (250, 400) #point 1
    pt2 = (250, 200) #point 2   

    color = (0, 0, 255) #red color in BGR
    thickness = 5 #thickness of the rectangle

    cv2.rectangle(image, pt1, pt2, color, thickness) #draw rectangle on the image

    cv2.imshow("Rectangle on image", image) #show the image with rectangle
    cv2.imwrite("rectangle on image.png", image) #save the image with rectangle         

    cv2.waitKey(0)
    cv2.destroyAllWindows()

