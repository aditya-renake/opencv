import cv2

image = cv2.imread("Phase 2(Image Resizing & Shaping)/avr.jpeg")

if image is None:
    print("Image not found")

else:
    print("Image loaded")

    resized = cv2.resize(image, (300, 300)) #always pass dimesions in tuple

    cv2.imshow("Original image", image)
    cv2.imshow("Resized image", resized)

    cv2.imwrite("resized image.png", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    