import cv2

# Image Path
img_path = r'Pics\\Round2_Crop.png'
centerList = []
# Reading image with OpenCv

c = 0
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 12, 12, 60)
edged = cv2.Canny(blur, 170, 200)
ret, thresh1 = cv2.threshold(edged, 80, 255, cv2.THRESH_BINARY) # Applying a threshold and converting the pixels to

contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    

    if len(approx) == 4:
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centerList.append((cX, cY))

        x, y, w, h = cv2.boundingRect(approx)
        cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
        # print([x, y, w, h])
        aspectRatio = float(w)/h
        if aspectRatio >= 0.8 and aspectRatio <= 1.20:
            # cv2.circle(img, (cX, cY), 5, (255, 255, 255), 1)
            cv2.putText(img, f'.', (cX, cY), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0))
            # cv2.putText(img, f'.', (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
            c += 1

print(centerList)
# cv2.imwrite(f'Pics\Output\output{i}.png', img)
cv2.imshow(f"Rects", img)
# cv2.imshow("Gray", gray)
# cv2.imshow("Thrsh", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()