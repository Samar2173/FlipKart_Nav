import cv2
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
    # Video Path
    vid_path = r'GitFiles\FlipKart_Nav\Vids\map.mp4'

    # Loading Video
    cap = cv2.VideoCapture(vid_path)

    # Reading frame by frame
    _, frame = cap.read()
    img_path = r'GitFiles\FlipKart_Nav\Pics\Output_V1.png'
    cv2.imwrite(img_path, frame)
    # File Path
    filename = r'GitFiles\FlipKart_Nav\Files\Co-ordinates_V1.csv' # For Round 1

    # Image Save Path
    img_save = r'GitFiles\FlipKart_Nav\Pics\Blank_V1.png' # For Round 1

    # Co-ordinates for Path
    inp_1 = (915, 704)
    inp_2  = (552, 226)

    # Main Execution
    main(filename, img_path, inp_1, inp_2, img_save)

