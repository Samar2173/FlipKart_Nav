import cv2
import numpy as np
import csv

class ImageProcess:
    def __init__(self, img_path, file_path):
        self.img_path = img_path
        self.file_path = file_path
        self.cords = []  # Empty list to store unique cords

    def cordsExtract(self):
        # Reading image with OpenCv
        # and processing it for better
        # extraction of contours and
        # corodinates
        img = cv2.imread(self.img_path)
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
        self.blank = np.zeros([h_img, w_img, 3], dtype = np.uint8)
        self.blank [:, :] = [0, 0, 0] 

        # Filtering through each contour and
        # then getting the coordinates to 
        # add to the above list
        area = set()
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.001 * cv2.arcLength(contour, True), True)

            # if len(approx) == 4:
            M = cv2.moments(contour)
            if M['m00'] > 3500 and M['m00'] < 6500:
                if M['m00'] == 0:
                    cX, cY = 0, 0,
                else:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                area.add(M['m00'])

                x, y, w, h = cv2.boundingRect(approx)
                
                # print([x, y, w, h])
                aspectRatio = float(w)/h
                if aspectRatio >= 0.8 and aspectRatio <= 1.20:
                    cv2.drawContours(self.blank, [approx], 0, (0, 0, 255), 2)
                    cv2.circle(self.blank, (cX, cY), 5, (255, 0, 0), 1)
                    if (cX, cY) not in self.cords:
                        self.cords.append([cX, cY])

        # cv2.imshow(f"Original", img)
        cv2.imshow(f"Rects", self.blank)

        # print(np.array(cords))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def imageSave(self, imgSave_path):
        cv2.imwrite(imgSave_path, self.blank)

    def cords2CSV(self):
        self.cords.sort()
        print("Creating CSV file...")

        header = [['x', 'y']]
        print("Writing CSV file...")
        with open(self.file_path, 'w') as file:
            
            writer = csv.writer(file)
            writer.writerows(header)
            writer.writerows(self.cords)

        file.close()
        print("CSV file ready")

if __name__ == '__main__':

    # Image Path
    img_path = r'Pics\Round1_Crop.png'

    # File Path
    filename = r'Files\Co-ordinates_1.csv'

    extraction = ImageProcess(img_path, filename)

    extraction.cordsExtract()

    img_save = r'Pics\Blank_1.png'
    extraction.imageSave(img_save)
    extraction.cords2CSV()