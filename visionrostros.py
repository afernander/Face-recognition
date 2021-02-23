'''
Para instalar la libreria cv2 debe ejecutar:
>> pip install opencv-python
>> pip install opencv-contrib-python
más información en OpenCV https://pypi.org/project/opencv-python/
'''

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

def crearRostros(imagenAnalizar, rostros):
    ROI_number = 0
    listarc = ls(".\\")
    #identificar que rostros se han leido
    for e in listarc:
        if (e=='ROI_{}.png'.format(ROI_number)):
            ROI_number+=1
    for (x, y, w, h) in rostros:
        ROI = imagenAnalizar[y:y+h, x:x+w]
        cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
        ROI_number += 1
    print("{} archivos creados...".format(len(rostros)))

#=================================================================
#función que muestra los rostos identificados
def verRostosImagen(imagenAnalizar, rostros):
    print("Encontrado {0} rostros en la imagen!".format(len(rostros)))

    #dibuja un rectangulo al rededor del rostro
    #color = (255,0,0) #BGR: azul
    color = (0,255,0) #BGR: verde
    #color = (0,0,255) #BGR: rojo
    grosor = 2

    for (x, y, w, h) in rostros:
        cv2.rectangle(imagenAnalizar, (x, y), (x+w, y+h), color, grosor)

    cv2.imshow("rostros encontrado", imagenAnalizar)
    print ("[esc] en la imagen para salir...")
    cv2.waitKey(0)
     

def pintarRostosImagen(imagenAnalizar, rostros):
    print("Encontrado {0} rostros en la imagen!".format(len(rostros)))

    #dibuja un rectangulo al rededor del rostro
    #color = (255,0,0) #BGR: azul
    color = (0,255,0) #BGR: verde
    #color = (0,0,255) #BGR: rojo
    grosor = 2

    for (x, y, w, h) in rostros:
        cv2.rectangle(imagenAnalizar, (x, y), (x+w, y+h), color, grosor)

    return imagenAnalizar 

#===========================================================0
# función que ver rostro por rostro (muestra 4 en este ejemplo)
def verSubRostros(imagenesRostros):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    #para instalar: pip install matplotlib

    print(type(imagenesRostros))
    print(type(imagenesRostros[0]))

    fig = plt.figure()
    num_rostro=0
    num=1
    num_rostro=0
    for i in imagenesRostros:
        a = fig.add_subplot(2, 2, num)
        num+=1
        a.set_title('Rostro {}'.format(i))
        imgplot = plt.imshow(imagenesRostros[num_rostro])
        num_rostro+=1
        #mostrar rostros individualmente
    plt.show()   
    print ("[esc] en la imagen para salir...")
    if(cv2.waitKey(0)):
        plt.close()

    


def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]