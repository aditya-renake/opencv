import cv2
image = cv2.imread("Phase 1/avr.jpeg")

if image is not None:
    h, w, c = image.shape
    print(f"Image loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")

else:
    print("Could not load image")