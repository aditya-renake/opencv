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
    print("Could not load image")






