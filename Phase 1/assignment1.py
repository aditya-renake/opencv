"""
import cv2
image = cv2.imread(input("Enter the location of the image = "))

if image is not None:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayscale image", gray)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_path = input("Enter location/name of the image you want to save =  ")
    cv2.imwrite(save_path, gray)

else:
    print("Could not load image")"""


import cv2

image_path = input("Enter the location of the image: ").strip()
image = cv2.imread(image_path)

if image is not None:
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Display the grayscale image (do NOT assign to gray, imshow returns None)
    cv2.imshow("grayscale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 3. Get save path from user and save
    save_path = input("Enter location/name of the image to save (e.g. output.jpg): ").strip()
    cv2.imwrite(save_path, gray)
    print(f"Image successfully saved to {save_path}")
else:
    print("Could not load image. Please check the file path.")






