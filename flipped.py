# flipped = cv2.flip(image, flipcode)
#flipcode = 0 means flipping around x-axis,
# flipcode = 1 means flipping around y-axis, 
#flipcode = -1 means flipping around both axes

import cv2

image = cv2.imread("Phase 2(Image Resizing & Shaping)/avr.jpeg")

if image is None:
    print("Image not found")
else:
    flipepd_horizontal = cv2.flip(image, 1) #flipping around y-axis
    flipped_vertical = cv2.flip(image, 0) #flipping around x-axis
    flipped_both = cv2.flip(image, -1) #flipping around both axes

    cv2.imshow("Original image", image)
    cv2.imshow("Flipped Horizontal", flipepd_horizontal)
    cv2.imshow("Flipped Vertical", flipped_vertical)
    cv2.imshow("Flipped Both", flipped_both)    

    cv2.imwrite("flipped_horizontal.png", flipepd_horizontal)
    cv2.imwrite("flipped_vertical.png", flipped_vertical)
    cv2.imwrite("flipped_both.png", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 