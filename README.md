# 数字图像处理HW2
- 林汉宁  自动化52 2150504042
- 提交日期：2019-03-05
 -----------------------------------
## 摘要
本次作业使用python面向对象方式编程，使用了opencv库。
针对图像配准问题，首先在两张图中手动选择7个配准点。之后计算变换矩阵H，再利用矩阵H实现图像的配准。其中代码的矩阵运算使用了numpy库函数，矩阵数据类型为mat
## 技术讨论
### 图像配准
#### 代码思路
首先定义Pic类与其内部函数，使用cov函数作为配准函数。定义矩阵类型点坐标，进行矩阵运算求得矩阵H，并利用H计算配准后图像。
#### 结果展示
![](http://ww1.sinaimg.cn/mw690/006tquCMly1g0s8mh6470j325d1m1b2h.jpg)
#### 源代码
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
        # cv.imshow("after rotate",new_img)
        # k = cv.waitKey(0) & 0xFF
        # if k == 27:         # 按下ESC退出
        #     cv.destroyAllWindows()
        # cv.imwrite('2_ROTATE.png',new_img)
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
	temp=P*P.T
	temp=temp.I
	H=Q*(P.T*temp)
	print("{}".format(H))
	pic_B=Pic("pic_A","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project2/Image B.jpg")
	pic_B.conv(H)



        
