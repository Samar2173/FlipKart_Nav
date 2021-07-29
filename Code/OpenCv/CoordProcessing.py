import cv2
import numpy as np
import pandas as pd

euclidean = lambda x1, y1, x2, y2 : (abs((x2 - x1) + (y2 - y1))) ** 0.5

class Data_Manupilation:
    # filename = 'Files\Co-ordinates.csv'
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        
        print("Processing..")
        for i in range(1, len(self.df.x)):
            if abs(self.df.x[i] - self.df.x[i-1]) < 1.5:
                self.df.x[i] = self.df.x[i-1]

            if abs(self.df.y[i] - self.df.y[i-1]) < 1.5:
                self.df.y[i] = self.df.y[i-1]

        self.df = self.df.drop_duplicates()
        self.df.sort_values(by = 'x')
        self.df.to_csv(filename, header = True, index = False)
        self.arr = self.df.values.tolist()
        
        

    def data2Dict(self):
        cordDict = {i[0] : [j[1] for j in self.arr if j[0] == i[0]] for i in self.arr}
        
        return cordDict

    def cordDefine(self, tup):
        calc = lambda a, b: abs((a - b)/b)
        
        for i in self.arr:
            if i == tup:
                return tuple(i)

            elif calc(i[0], tup[0]) < 0.01:
                if calc(i[1], tup[1]) < 0.01:
                    print(i, tup, calc(i[1], tup[1]))
                    return tuple(i)
                    

img = cv2.imread(r'Pics\Blank2.png')

filename = 'Files\Co-ordinates.csv'
data = Data_Manupilation(filename)
dict = data.data2Dict()
print(dict)

inp_1 = (328, 402)
inp_2 = (399, 329)
cords_1 = data.cordDefine(inp_1)
cords_2 = data.cordDefine(inp_2)

h = (euclidean(*cords_1, *cords_2) // 2) - 1

print(h)

if cords_1 != None and cords_2 != None:
    cv2.circle(img, cords_1, 5, (255, 250, 0), 1)
    cv2.circle(img, cords_2, 5, (0, 250, 0), 1)
    cv2.line(img, cords_1, cords_2, (0, 255, 0), 2)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

else:
    print("No appropriate data found!!")