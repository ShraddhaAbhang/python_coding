import cv2
import numpy as np

img = cv2.imread("image_processing_input\\dog_img.jpg")

def edge_dect(img):
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # blurred = cv2.GaussianBlur(src=gray_img, ksize=(5, 7), sigmaX=1.0)
    kernel = np.array([[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]])
    
    sharped = cv2.filter2D(img, -1, kernel)

    gray_img = cv2.cvtColor(sharped, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("gray_image", gray_img)


    # cv2.imwrite("gray_scale_image.jpg", gray_img)

    # cv2.waitKey(0)

    # edges = cv2.Canny(blurred, 70, 100) 
    edges = cv2.Canny(gray_img, 70, 100) 


    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask_img = np.zeros_like(edges)

    area_threashold = 10


    for contour in contours:

        area = cv2.contourArea(contour)
        if area >= area_threashold:
            cv2.drawContours(mask_img, [contour], -1, (255), thickness = cv2.FILLED)
    
    new_img = cv2.bitwise_and(edges, mask_img)


    # cv2.imshow("Mask_Img", mask_img)
    cv2.imshow("New_Img", new_img)
    cv2.imshow("Edges", edges)
    cv2.imshow("Sharpen_Img", sharped)
    # cv2.imshow("Img", img)
    cv2.waitKey(0)

    # print(edges)


    # return blurred, edges, 

edge_dect(img)
