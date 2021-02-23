'''
Para instalar la libreria cv2 debe ejecutar:
>> pip install opencv-python
>> pip install opencv-contrib-python
más información en OpenCV https://pypi.org/project/opencv-python/
'''
import os
import cv2
from os import scandir, getcwd

#Función que realiza la segmentación de rostros
def detectarRostros(imagenAnalizar):
    # Crear el reconocedor haar cascade
    '''
    Una cascada de Haar es un clasificador que se utiliza para
    detectar el objeto para el que ha sido entrenado
    '''
    entrenamiento ='data/haarcascade_frontalface_default.xml'
    #entrenamiento = "haarcascade_frontalface_default.xml"
    clasificadorRostros = cv2.CascadeClassifier(entrenamiento)
    imagenGris = cv2.cvtColor(imagenAnalizar, cv2.COLOR_BGR2GRAY)
    
    # Rostros detectados imagenAnalizar
    rostros = clasificadorRostros.detectMultiScale(
        imagenGris,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    imagenesRostros = []
    for (x, y, w, h) in rostros:
        ROI = imagenAnalizar[y:y+h, x:x+w]
        imagenesRostros.append(ROI)

    return [rostros, imagenesRostros]

#==========================================================
# función que genera archivos de imagenes por cada rostro identificado
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"Imagenes conocidos")
def crearRostros(imagenAnalizar, rostros,f):
    
    for (x, y, w, h) in rostros:
        ROI = imagenAnalizar[y:y+h, x:x+w]
        cv2.imwrite(f,ROI)
   

def main():
    img=[]
    
    for i in ls("D:\Escritorio\Parcial 3-Alejandro Fernandez Restrepo\Imagenes conocidos\Trump"):
        img.append("D:\Escritorio\Parcial 3-Alejandro Fernandez Restrepo\Imagenes conocidos\Trump\\"+i)
        print(i)
    num=len(img)
    #for i in (0,num-1):
    i=8
    imagenAnalizar = cv2.imread(img[i])

    [dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar) 


    crearRostros(imagenAnalizar, dataRostros,img[i])#

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

if __name__ == '__main__':
    main()