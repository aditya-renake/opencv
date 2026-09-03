import cv2

image = cv2.imread("Phase 2(Image Drawing Functions)/avr.jpeg")

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    pt1 = (50, 100) #point 1
    pt2 = (400, 400) #point 2   
    color = (255, 0, 0) #blue color in BGR
    thickness = 5 #thickness of the line

    cv2.line(image, pt1, pt2, color, thickness) #draw line on the image 
    cv2.imshow("Line on image", image) #show the image with line
    cv2.imwrite("line on image.png", image) #save the image with line       

    cv2.waitKey(0)
    cv2.destroyAllWindows()