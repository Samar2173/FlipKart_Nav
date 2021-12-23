'''
To process image and extract coordinates
and save to .csv

-Flipkart Navogation
Author - Samar .K
'''

import csv
from cv2 import cv2
import numpy as np

class ImageProcess:
    '''Class to process image and extract coordinates'''

    def __init__(self, img_path, file_path):
        self.img_path = img_path
        self.file_path = file_path
        self.cords = []  # Empty list to store unique cords
        self.blank = None

    def cords_extract(self):
        '''Reading image with OpenCv
        and processing it for better
        extraction of contours and
        corodinates'''

        img = cv2.imread(self.img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.bilateralFilter(gray, 13, 73, 95)
        edged = cv2.Canny(blur, 47, 170)
        thresh1 = cv2.adaptiveThreshold(edged, 255\
            , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)

        # Fetching and drawing contours
        contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(img, contours, 0, (0, 0, 255), 2)
        # cv2.imshow('Contours', img)

        # Creating white background image with
        # dimesions similar to input image
        # for mapping the coordinates and
        # drawing the coordinates
        h_img, w_img, _ = img.shape
        self.blank = np.zeros([h_img, w_img, 3], dtype=np.uint8)
        self.blank [:, :] = [0, 0, 0]

        # Filtering through each contour and
        # then getting the coordinates to
        # add to the above list
        area = set()
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.001 * cv2.arcLength(contour, True), True)

            # if len(approx) == 4:
            moment = cv2.moments(contour)
            # if M['m00'] > 1250 and M['m00'] < 11000:
            if moment['m00'] > 4500 and moment['m00'] < 11000:  #For chute box Detection
            # if True:
                if moment['m00'] == 0:
                    c_x, c_y = 0, 0
                else:
                    c_x = int(moment["m10"] / moment["m00"])
                    c_y = int(moment["m01"] / moment["m00"])

                area.add(moment['m00'])

                _, _, width, height = cv2.boundingRect(approx)

                # print([x, y, width, h])
                aspect_ratio = float(width)/height
                if aspect_ratio >= 0.8 and aspect_ratio <= 1.20:
                    cv2.drawContours(self.blank, [approx], 0, (0, 0, 255), 2)
                    cv2.circle(self.blank, (c_x, c_y), 5, (255, 0, 0), 1)
                    if (c_x, c_y) not in self.cords:
                        self.cords.append([c_x, c_y])

        # cv2.imshow(f"Original", img)
        cv2.imshow(f"Rects", self.blank)

        # print(np.array(cords))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def image_save(self, img_save_path):
        '''Save image to given path'''
        cv2.imwrite(img_save_path, self.blank)

    def cords_to_csv(self):
        '''Convert coordinates to .csv'''
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
    IMG_PATH = r'//home/rez3liet/Projects/Flipkart/FlipKart_Nav/Pics/map_Moment.jpg' # For Round 1

    # File Path
    FILENAME = r'/home/rez3liet/Projects/Flipkart/FlipKart_Nav/\
        Files/Co-ordinates_map.csv' # For Round 1

    EXTRACTOR = ImageProcess(IMG_PATH, FILENAME)

    EXTRACTOR.cords_extract()

    IMG_SAVE = r'/home/rez3liet/Projects/Flipkart/FlipKart_Nav/Pics/bag_output_1.png' # For Round 1
    EXTRACTOR.image_save(IMG_SAVE)
    # EXTRACTOR.cords_to_csv()
