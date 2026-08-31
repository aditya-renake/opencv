import cv2
image = cv2.imread("Phase 1/avr.jpeg")

if image is not None:
    sucess = cv2.imwrite("output_python.png", image)
    if sucess:
        print("'Image saved sucessfulyy as output_python.png'")
    else:
        print("Failed to save an image")

else:
    print("error: could not load an image")
