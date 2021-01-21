import cv2

img_src = cv2.imread("./images/portrait.jpg", cv2.IMREAD_COLOR)

h = img_src.shape[0]
w = img_src.shape[1]

print(img_src.shape[0])