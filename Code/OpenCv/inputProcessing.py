import cv2
import numpy as np
import csv

# Image Path
img_path = r'Pics\Round2_Crop.png'

cords = []  # Empty list to store unique cords

# Reading image with OpenCv
# and processing it for better
# extraction of contours and
# corodinates
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 12, 12, 60)
edged = cv2.Canny(blur, 170, 200)
ret, thresh1 = cv2.threshold(edged, 80, 255, cv2.THRESH_BINARY) 

# Fetching and drawing contours 
contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, 0, (0, 0, 255), 2)

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
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.0001 * cv2.arcLength(contour, True), True)

    M = cv2.moments(contour)
    if M['m00'] == 0:
        cX, cY = 0, 0,
    else:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    x, y, w, h = cv2.boundingRect(approx)
    
    # print([x, y, w, h])
    aspectRatio = float(w)/h
    if aspectRatio >= 0.8 and aspectRatio <= 1.20:
        cv2.drawContours(blank, [approx], 0, (0, 0, 255), 2)
        cv2.circle(blank, (cX, cY), 5, (255, 0, 0), 1)
        if (cX, cY) not in cords:
            cords.append([cX, cY])

cords.sort()
# cv2.imshow(f"Original", img)
cv2.imshow(f"Rects", blank)
cv2.imwrite("Pics/Blank2.png", blank)

# print(np.array(cords))
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Creating CSV file...")
filename = 'Files\Co-ordinates.csv'

header = [['x', 'y']]
print("Writing CSV file...")
with open(filename, 'w') as file:
    
    writer = csv.writer(file)
    writer.writerows(header)
    writer.writerows(cords)

file.close()
print("CSV file ready")
