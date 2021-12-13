import cv2
import numpy as np

img=cv2.imread("test.jpeg",cv2.IMREAD_COLOR)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
h=img.shape[0]
w=img.shape[1]
for x in range(0,w,2):
    for y in range(0,h,2):
        sum=0
        for i in range(0,1):
            for j in range(0,1):
                if((y+j<h)&(x+i<w)):
                    sum += img1[y+j,x+i]
        if ((y+1<h) & (x+1<w)):
            if(sum>192):
                img2[y+1,x+1] = 255
                img2[y+1,x] = 255
                img2[y,x+1] = 255
                img2[y,x] = 255
            elif(sum>128):
                img2[y+1,x+1] = 255
                img2[y+1,x] = 255
                img2[y,x+1] = 255
                img2[y,x] = 0
            elif(sum>64):
                img2[y+1,x+1] = 255
                img2[y+1,x] = 255
                img2[y,x+1] = 0
                img2[y,x] = 0
            else:
                img2[y+1,x+1] = 255
                img2[y+1,x] = 0
                img2[y,x+1] = 0
                img2[y,x] = 0
cv2.imshow('Color',img)
cv2.imshow('Dithered',img2)
cv2.waitKey(0)
CV2.destroyAllWindows()
