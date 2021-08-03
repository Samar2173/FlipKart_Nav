from inputProcessing import ImageProcess
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
    img_path = r'Pics\Round1_Crop.png' # For Round 1
    # img_path = r'Pics\Round2_Crop.png' # For Round 2

    # File Path
    filename = r'Files\Co-ordinates_1.csv' # For Round 1
    # filename = r'Files\Co-ordinates_2.csv' # For Round 2

    # Image Save Path
    img_save = r'Pics\Blank_1.png' # For Round 1
    # img_save = r'Pics\Blank_2.png' # For Round 2

    # Co-ordinates for Path
    inp_1 = (778, 116)
    inp_2  = (207, 744)

    # Main Execution
    main(filename, img_path, inp_1, inp_2, img_save)