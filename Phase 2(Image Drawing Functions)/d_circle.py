import cv2

image = cv2.imread("Phase 2(Image Drawing Functions)/avr.jpeg")
if image is None:
    print("Image not found")        
else:
    print("Image loaded")
    cv2.circle(image, (150, 150), 50, (255, 0, 0), -1 ) #draw circle on the image

    cv2.imshow("Circle on image", image) #show the image with circle
    cv2.imwrite("circle on image.png", image) #save the image with circle         

    cv2.waitKey(0)
    cv2.destroyAllWindows()


   



