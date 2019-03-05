import cv2 as cv
import math
import numpy

class Pic:
    def __init__(self, name, path):
         self.name=name
         self.path=path
         self.img=cv.imread(path)
    def show(self):
        cv.imshow("{}".format(self.name),self.img)
        k = cv.waitKey(0) & 0xFF
        if k == 27:         # 按下ESC退出
            cv.destroyAllWindows()
    def conv(self,H):
        dimensions=self.img.shape
        height = dimensions[0]
        width = dimensions[1]
        channels = dimensions[2]
        new_img=numpy.zeros((height,width,channels), numpy.uint8)
        for i in range(height):
            for j in range(width):
                temp=[i,j,1]*H
                # print("[i,j,1]:{}".format([i,j,1]))
                # print("new={}".format(temp[0,0]))
                if int(temp[0,0])>=height or int(temp[0,1])>=width:
                    continue
                new_img[int(temp[0,0]),int(temp[0,1]),:]=self.img[i,j,:]
        cv.imshow("after rotate",new_img)
        k = cv.waitKey(0) & 0xFF
        if k == 27:         # 按下ESC退出
            cv.destroyAllWindows()
        cv.imwrite('2_ROTATE.png',new_img)

# pick dot
A_dots = numpy.mat([
    [1022.87500000000,1814.25000000000,1],
    [1023.62500000000,2125.12500000000,1],
    [1211.37500000000,2240.12500000000,1],
    [1371.62500000000,2318.12500000000,1],
    [2427.87500000000,1613.62500000000,1],
    [2901.62500000000,1076.37500000000,1],
    [973.375000000000,1021.37500000000,1]]) 

B_dots = numpy.mat([
    [708.125000000000,1323.12500000000,1],
    [628.875000000000,1624.87500000000,1],
    [780.375000000000,1782.87500000000,1],
    [914.875000000000,1901.12500000000,1],
    [2117.62500000000,1489.87500000000,1],
    [2713.87500000000,1093.37500000000,1],
    [863.125000000000,544.625000000000,1]]) 
Q=A_dots.T
P=B_dots.T
print("{}".format(Q.shape))
print("{}".format(P.shape))
temp=P*P.T
temp=temp.I
H=Q*(P.T*temp)
print("{}".format(H))

# pic_A=Pic("pic_A","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project2/Image A.jpg")
pic_B=Pic("pic_A","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project2/Image B.jpg")
pic_B.conv(H)


