# FlipKart_Nav

## Required Libraries:
 pandas
 cv2
 numpy
 csv

## Executing Files
### [main.py](https://github.com/Samar2173/FlipKart_Nav/blob/main/Code/main.py)
To run the code execute main.py file

### [live_image.py](https://github.com/Samar2173/FlipKart_Nav/blob/main/Code/live_image.py)
This file deals with the input image of the map and extracts and
stores the center coordinates of the squares inside the grid to csv file, 
while creating a new image (initially blank with same dimensions) with the
contours of sqaure with their center point.

### [astar_cv2_sides.py](https://github.com/Samar2173/FlipKart_Nav/blob/main/Code/astar_cv2_sides.py)
This file contains code to clean data from csv file and display given
coordinates on the given image path(blank image) and also returning a 
dictionary with keys as number of stop-points/checkpoints from 0 to n
n being len(dictionary.keys) - 1 and each key having a coressponding 
coordinate value in (x, y) format. DOES NOT CONTAIN DIAGONALS.

### [astar_cv2_diagonal.py](https://github.com/Samar2173/FlipKart_Nav/blob/main/Code/astar_cv2_diagonals.py)
Same as astar_cv2_sides.py but also considers diagonals for optimal path.

### [live_vid.py](https://github.com/Samar2173/FlipKart_Nav/blob/main/Code/live_vid.py)
This file helps in taking frames from video or live stream an helps in giving out the path with
help of live_img.py and astar_cv2_siddes.py.

## Images Round 1 Only

### Cropped Input Image
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Round1_Crop.png)

### Blank with Contours and Center Points
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Blank_1.png)

### Path Output (Diagonals)
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Output_1.png)

### Video Input
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Output_V1.png)

### Video Blank with Contours and Center Points
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Blank_V1.png)

### Video Output (Sides)
![Alt text](https://github.com/Samar2173/FlipKart_Nav/blob/main/Pics/Path_V1.png)

## Dictionary Output
### Path Found... {0: (778, 114), 1: (700, 191), 2: (700, 271), 3: (700, 352), 4: (700, 432), 5: (700, 511), 6: (700, 588), 7: (621, 665), 8: (538, 744), 9: (457, 744), 10: (376, 744), 11: (291, 744), 12: (207, 744)}
