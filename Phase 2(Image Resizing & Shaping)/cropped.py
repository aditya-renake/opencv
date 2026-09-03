import cv2
image = cv2.imread("Phase 2(Image Resizing & Shaping)/avr.jpeg")

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    cropped = image[100:400, 100:400] #cropping the image
    
    cv2.imshow("Original image", image)
    cv2.imshow("Cropped image", cropped)

    cv2.imwrite("cropped image.png", cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()