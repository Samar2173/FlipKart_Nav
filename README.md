# FlipKart_Nav

## Required Libraries:
 pandas
 cv2
 numpy
 csv
 
## To run the code execute main.py file

## inputProcessing.py delas with the input image of the map and extracts and
## stores the center coordinates of the squares inside the grid to csv file, 
## while creating a new image (initially blank with same dimensions) with the
## contours of sqaure with their center point.

## astar_cv2.py contains code to clean data from csv file and display given
## coordinates on the given image path(blank image) and also returning a 
## dictionary with keys as number of stop-points/checkpoints from 0 to n
## n being len(dictionary.keys) - 1 and each key having a coressponding 
## coordinate value in (x, y) format.
