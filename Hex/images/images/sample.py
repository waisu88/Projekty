import cv2
import imutils
# print(f""base_image.image)
img = imutils.url_to_image("http://127.0.0.1:8000/media/uploads/2023/02/18/szymon.JPG")
print(img)
img = cv2.imread(img)
down_width = 860
down_height = 640
down_points = (down_width, down_height)

resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)



gray = cv2.cvtColor(resized_down, cv2.COLOR_BGR2GRAY)
ret, tresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary', tresh1)
# cv2.imshow('Original image',img)
# cv2.imshow('Gray image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()





