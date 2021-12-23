import cv2
import numpy as np

img_path = r'/home/rez3liet/Projects/Flipkart/FlipKart_Nav/Pics/bag_ip.png'
cords = []


# Reading image with OpenCv
# and processing it for better
# extraction of contours and
# corodinates
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 13, 73, 95) 
edged = cv2.Canny(blur, 47, 170)  
thresh1 = cv2.adaptiveThreshold(edged, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10) 

# Fetching and drawing contours 
contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', img)

cv2.imwrite('/home/rez3liet/Projects/Flipkart/FlipKart_Nav/Pics/bag_output_1.png', img)
# Creating white background image with
# dimesions similar to input image
# for mapping the coordinates and
# drawing the coordinates
h_img, w_img, _ = img.shape
blank = np.zeros([h_img, w_img, 3], dtype = np.uint8)
blank [:, :] = [0, 0, 0] 

# Filtering through each contour and
# then getting the coordinates to 
# add to the above list
area = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.001 * cv2.arcLength(contour, True), True)

    # if len(approx) == 4:
    M = cv2.moments(contour)
    if M['m00'] > 1000 :
    # if True:
        if M['m00'] == 0:
            cX, cY = 0, 0,
        else:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

        area.append(M['m00'])

        x, y, w, h = cv2.boundingRect(approx)
        
        # print([x, y, w, h])
        aspectRatio = float(w)/h
        if aspectRatio >= 0.9 and aspectRatio <= 1.10:
            cv2.drawContours(blank, [approx], 0, (0, 0, 255), 2)
            cv2.circle(blank, (cX, cY), 5, (255, 0, 0), 1)
            if (cX, cY) not in cords:
                cords.append([cX, cY])

# cv2.imshow(f"Original", img)
cv2.imshow(f"Rects", blank)

# print(np.array(cords))
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(set(area))