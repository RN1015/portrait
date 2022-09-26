import cv2

# img_location = r"testimage_1.jpeg"

filename = "RDJ.jpg"

img = cv2.imread(filename, 30)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_img = 253 - gray_image

blurred_img = cv2.GaussianBlur(inverted_img, (15, 15), 0)

inverted_blur_img = 253 - blurred_img

sketch_img = cv2.divide(gray_image , inverted_blur_img, scale = 253.0)

cv2.imshow('Original Image', img)
cv2.imshow('Sketch Image', sketch_img)

cv2.waitKey(0)