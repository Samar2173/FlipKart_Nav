from live_image import ImageProcess
from astar_cv2_sides import findPath

def main(file_path, img_path, startPoint, goalPoint, img_save_path = None):
    r_path = img_path
    data = ImageProcess(img_path, file_path)
    data.cordsExtract()

    if img_save_path != None: 
        data.imageSave(img_save_path)
        r_path = img_save_path

    data.cords2CSV()

    path = findPath(r_path, file_path, startPoint, goalPoint)

    print("Path Found...", path)

if __name__ == '__main__':
    # Image Path
    img_path = r'GitFiles\FlipKart_Nav\Pics\map_moment.jpg' # For Round 1
    # img_path = r'Pics\Round2_Crop.png' # For Round 2

    # File Path
    filename = r'GitFiles\FlipKart_Nav\Files\Co-ordinates_1F.csv' # For Round 1
    # filename = r'Files\Co-ordinates_2.csv' # For Round 2

    # Image Save Path
    img_save = r'GitFiles\FlipKart_Nav\Pics\Blank_1.png' # For Round 1
    # img_save = r'Pics\Blank_2.png' # For Round 2

    # Co-ordinates for Path
    inp_1 = (552, 226)
    inp_2  = (1097, 703)

    # Main Execution
    main(filename, img_path, inp_1, inp_2, img_save)