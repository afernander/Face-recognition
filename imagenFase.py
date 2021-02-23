import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.registration import phase_cross_correlation
from skimage.registration._phase_cross_correlation import _upsampled_dft
from scipy.ndimage import fourier_shift

#image = data.camera()
import sys
import cv2
def imgxfase(img1 , img2,ver):
    rutaImagen = img1
    imagenAnalizar = cv2.imread(rutaImagen)
    image = cv2.cvtColor(imagenAnalizar, cv2.COLOR_BGR2GRAY)

    shift = (-220.4, 133.32)
    # The shift corresponds to the pixel offset relative to the reference image
    #edi offset_image = fourier_shift(np.fft.fftn(image), shift)
    #edi offset_image = np.fft.ifftn(offset_image)
    #edi print(f"Known offset (y, x): {shift}")


    # Valores de entrada
    rutaImagen = img2
    imagenAnalizar = cv2.imread(rutaImagen)
    imagenGris = cv2.cvtColor(imagenAnalizar, cv2.COLOR_BGR2GRAY)
    offset_image = cv2.cvtColor(imagenAnalizar, cv2.COLOR_BGR2GRAY)

    # pixel precision first
    shift, error, diffphase = phase_cross_correlation(image, offset_image)
    if(ver.upper()=="Y"):
        fig = plt.figure(figsize=(8, 3))
        ax1 = plt.subplot(1, 3, 1)
        ax2 = plt.subplot(1, 3, 2, sharex=ax1, sharey=ax1)
        ax3 = plt.subplot(1, 3, 3)
    
        ax1.imshow(image, cmap='gray')
        ax1.set_axis_off()
        ax1.set_title('Reference image')

        ax2.imshow(offset_image.real, cmap='gray')
        ax2.set_axis_off()
        ax2.set_title('Offset image')





    # Show the output of a cross-correlation to show what the algorithm is
    # doing behind the scenes
    image_product = np.fft.fft2(image) * np.fft.fft2(offset_image).conj()
    #image_product = np.fft.fft2(image) * np.fft.fft2(imagenGris).conj()

    cc_image = np.fft.fftshift(np.fft.ifft2(image_product))
    if(ver.upper()=="Y"):
        ax3.imshow(cc_image.real)
        ax3.set_axis_off()
        ax3.set_title("Cross-correlation")

        plt.show()
    print("Maximo valor:" ,abs((cc_image.real.max()-723190206.0)))

    #print(f"Detected pixel offset (y, x): {shift}")

    # subpixel precision
    shift, error, diffphase = phase_cross_correlation(image, offset_image)
    data=[]
    data.append(diffphase)
    data.append(shift)
    data.append(error)
    #print("diffphase :",diffphase)
    #print("shift:", shift)
    #print("Error : " , error)
    if(ver.upper()=="Y"):
        fig = plt.figure(figsize=(8, 3))
        ax1 = plt.subplot(1, 3, 1)
        ax2 = plt.subplot(1, 3, 2, sharex=ax1, sharey=ax1)
        ax3 = plt.subplot(1, 3, 3)
    
        ax1.imshow(image, cmap='gray')
        ax1.set_axis_off()
        ax1.set_title('Reference image')

        ax2.imshow(offset_image.real, cmap='gray')
        ax2.set_axis_off()
        ax2.set_title('Offset image')


    # Calculate the upsampled DFT, again to show what the algorithm is doing
    # behind the scenes.  Constants correspond to calculated values in routine.
    # See source code for details.
    cc_image = _upsampled_dft(image_product, 150, 100, (shift*100)+75).conj()
    if(ver.upper()=="Y"):
        ax3.imshow(cc_image.real)
        ax3.set_axis_off()
        ax3.set_title("Supersampled XC sub-area")
        plt.show()

    imx = cc_image.max()
    #print('max: ',imx)
    data.append(imx)
    

    #print(f"Detected subpixel offset (y, x): {shift}")
    return data