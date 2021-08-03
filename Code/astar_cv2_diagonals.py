from queue import PriorityQueue
import pandas as pd
import cv2

class A_Star:
    def __init__(self, filename, start, goal):
        # Converting csv to dictionary
        self.filename = filename
        self.df = pd.read_csv(filename)
        self.dict = self.csv2Dict()

        self.start = self.arrayCord(start)
        self.goal = self.arrayCord(goal)
        self.g = 0
        self.h = float("inf")
        self.f = self.g + self.h
        self.pathList = [self.start]
        self.pathDict = {self.g : self.start}
        print("Initializing Completed!!!")

    def csv2Dict(self):
        print("Processing Data...")
        for i in range(1, len(self.df.x)):
            if abs(self.df.x[i] - self.df.x[i-1]) < 1.5:
                self.df.x[i] = self.df.x[i-1]

            if abs(self.df.y[i] - self.df.y[i-1]) < 1.5:
                self.df.y[i] = self.df.y[i-1]

        self.df = self.df.drop_duplicates()
        self.df.sort_values(by = 'x')
        # df_new = self.df.groupby(['x']).y.count()[lambda k: k < 5]
        # values = df_new.index.to_list()
        # self.df = self.df[self.df.x.isin(values) == False]
        self.df.to_csv(self.filename, header = True, index = False)
        self.arr = self.df.values.tolist()
        self.arr.sort()
        cordDict = {i[0] : [j[1] for j in self.arr if j[0] == i[0]] for i in self.arr}

        return cordDict

    def arrayCord(self, cord):
        # Converting given co-ordinates into
        # suitable co-ordinates belonging to array
        if cord in self.arr:
            return cord

        else:
            xC, yC = cord

            # For x
            keys = list(self.dict.keys())
            for i in range(len(keys)):
                if xC <= keys[i]:
                    if abs(keys[i] - xC) >= abs(keys[i-1] - xC):
                        x = keys[i-1]
                    elif i == 0:
                        x = keys[i] 
                    else:
                        x = keys[i]
                    break

                else:
                    x = keys[-i]
            
            # For y
            for i in range(len(self.dict[x])):
                if yC <= self.dict[x][i]:
                    if abs(self.dict[x][i] - yC) >= abs(self.dict[x][i-1] - yC):
                        y = self.dict[x][i-1]
                        
                    elif i == 0:
                        y = self.dict[x][i] 
                    else:
                        y = self.dict[x][i]
                    break

                else:
                    y = self.dict[x][-1]

            # print(x, y)
            return (x, y)        

    def pathVerify(self, coordinate):
        if self.euclidean(coordinate, self.pathList[-1]) < 140:
            return True
        return False
    
    def euclidean(self, current, goal):
        # To find euclidean distance
        x1, y1 = current
        x2, y2 = goal
        res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        # print(current, (x2, y2))
        return round(res)

    def neighborClean(self, cord_list, comparator):
        cord_list.sort()
        maxVal = max(cord_list)
        minVal = min(cord_list)
        avgCom = comparator

        if (maxVal - minVal) > 200:
            if (maxVal - avgCom) > (avgCom - minVal):
                cord_list.pop(-1)
            else:
                cord_list.pop(0)
        
        return cord_list

    # Inclusive of digonals also
    def neighbors(self, current):
        # Only when current is part of array coordinates
        neighborList = []
        
        xC, yC = self.arrayCord(current)
        # print((xC, yC))
        keys = list(self.dict.keys())
        # For x when y is constant
        if xC in keys:
            # print("In Keys", current)
            loc = keys.index(xC)
            if loc > 0 and loc < len(keys) - 1:
                x_list = [keys[loc - 1], keys[loc], keys[loc + 1]]
            elif loc == 0:
                x_list = [keys[loc], keys[loc + 1]]
            elif loc == len(keys) -1:
                x_list = [keys[loc - 1], keys[loc]]
        
        # print(x_list)
        # For y when x is constant
        y_all = []
        for i in x_list:

            if yC in self.dict[i]:
                loc = self.dict[i].index(yC)
                yCI = yC
            else:
                _, yCI = self.arrayCord((i, yC))
                if abs(yCI - yC)/max(yCI, yC) > 0.2:
                    r = x_list.index(i)
                    x_list.pop(r)
                    continue
            
            loc = self.dict[i].index(yCI)
            if loc > 0 and loc < len(self.dict[i]) - 1:
                y_list = [self.dict[i][loc - 1], self.dict[i][loc],  self.dict[i][loc + 1]]
            elif loc == 0 and len(self.dict[i]) >= 2:
                y_list = [self.dict[i][loc], self.dict[i][loc + 1]]
            elif loc == 0 and len(self.dict[i]) < 2:
                y_list = [self.dict[i][loc]]
            elif loc == len(self.dict[i]) -1:
                y_list = [self.dict[i][loc - 1], self.dict[i][loc]]
            
            y_list = self.neighborClean(y_list, self.dict[i][loc])
            y_all.extend(y_list)
        # print(i, y_list)
        neighborList = [self.arrayCord((j, k)) for j in x_list for k in set((y_all))]
        
        neighborSet = set((neighborList))
        # print((xC, yC) in neighborSet)
        return neighborSet

    def hVal(self):        
        neighbors_list = self.neighbors(self.pathList[-1])
        # print(neighbors_list)
        h_dict = {}
        for i in neighbors_list:
            dist = self.euclidean(i, self.goal)
            h_dict[i] = dist
            # print(i, self.euclidean(i))
        while True:
            cord = min(h_dict.keys(), key=(lambda k: h_dict[k]))
            if self.pathVerify(cord):
                break
            else:
                h_dict.pop(cord)

        self.pathDict[self.g] = cord
        self.pathList.append(cord)

        return h_dict[cord]

    def pathCalc(self):
        self.g += 1
        self.h = self.hVal()
        self.f = self.g + self.h
        if self.h == 0:
            # print(self.h)
            return False
        elif self.g > 1:
            if self.pathDict[self.g] == self.pathDict[self.g-2]:
                print("Repetation")
                return False

        return True

def findPath(img_path, file_path, start, goal):
    
    path = A_Star(file_path, start, goal)

    flag = True
    while flag:
        flag = path.pathCalc()

    img = cv2.imread(img_path)
    # print(path.pathDict)

    for i in path.pathDict.values():
        cv2.circle(img, i, 5, (0, 250, 255), 10)

    for i in (path.arrayCord(start), path.arrayCord(goal)):
        cv2.putText(
            img, #numpy array on which text is written
            str(i), #text
            i, #position at which writing has to start
            cv2.FONT_HERSHEY_SIMPLEX, #font family
            1, #font size
            (255, 255, 255, 255), #font color
            1)

    cv2.circle(img, start, 5, (0, 250, 0), 10)
    cv2.circle(img, goal, 5, (0, 0, 255), 10)

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(r'Pics\Output_F1.png', img)

    return path.pathDict

if __name__ == '__main__':

    img = r'GitFiles\FlipKart_Nav\Pics\Blank_1.png'
    file = r'GitFiles\FlipKart_Nav\Files\Co-ordinates_1.csv'
    inp_1 = (200, 800)
    inp_2  = (850, 105)

    
    findPath(img, file, inp_1, inp_2)
    