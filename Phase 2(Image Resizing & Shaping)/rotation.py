# M = cv2.getRotationMatrix2D(center, angle, scale)
#rotated_image = cv2.warpAffine(image, M, (width, height))


"""always rotate the image in the center of the image

    center point = (width//2, height//2)

"""

import cv2

image = cv2.imread("Phase 2(Image Resizing & Shaping)/avr.jpeg")

if image is None:
    print("Image not found")
else:

    (h, w) = image.shape[:2] #shape of the image, this is called shape attribute of the image, it returns a tuple of 3 values (height, width, channels)

    center = (w//2, h//2) #center of the image

    M = cv2.getRotationMatrix2D(center, 90, 1.0) #rotation matrix, angle is in degrees, scale is 1.0 means no scaling
    rotated = cv2.warpAffine(image, M, (w, h)) #warpAffine function is used to apply the rotation matrix to the image

    cv2.imshow("Original image", image)
    cv2.imshow("Rotated image", rotated)
    cv2.imwrite("rotated image.png", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()