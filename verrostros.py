import numpy as np 
import cv2
import os
from PIL import Image
from os import scandir, getcwd
from os import remove
import sys
def main():
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for i in ls(".\Imagenes conocidos\Daniel Cifuentes\\"):
        ruta=".\Imagenes conocidos\Daniel Cifuentes\\"+i
        img=cv2.imread(ruta)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5,minSize=(30, 30))
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

if __name__ == '__main__':
    main()