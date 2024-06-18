# Read a image using Opencvs

import cv2

img = cv2.imread("dog_img.jpg")
# img = cv2.imread("db_details_sql.jpg",0)

cv2.imshow("image", img)

cv2.imwrite("original_image.jpg", img)

cv2.waitKey(0)

print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray_image", gray_img)

cv2.imwrite("gray_scale_image.jpg", gray_img)

cv2.waitKey(0)
# print(gray_img)

cv2.destroyAllWindows()