#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

import cv2
image = cv2.imread("Phase 1/avr.jpeg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Grayscale Image", gray)
    gray1 = cv2.imwrite("grayscale image avr.png", gray) #we saved the grayscale image we got
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Could not load the image")
    



