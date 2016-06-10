from SimpleCV import Image, Camera, Display, Image, Color
import time
import matplotlib.pyplot as plt

cam = Camera()
img = cam.getImage()
img.save('lunar.png')
time.sleep(4)
#img.show()

imgGray = img.grayscale()
imgGray.save('lunar_gris.png')


hist = imgGray.histogram(255)
plt.figure(1)
plt.stem(hist)
plt.axis('tight')
plt.title('Escala de grises')
plt.savefig('histograma_gris.png')
#plt.show('histgris.png')

(red, green, blue) = img.splitChannels(False)

red_hist = red.histogram(255)
green_hist = green.histogram(255)
blue_hist = blue.histogram(255)
plt.figure(2)
#plt.subplot(311)
plt.stem(red_hist)
plt.title('Red histogram')
plt.axis('tight')
plt.savefig('hist(red).png')

imagen=Image("lunar.png")
#imagen.show()
img_bin=imagen.sideBySide(imagen.binarize() )
img_bin.save('lunar_binario.png')

imgbin=imagen.binarize()

#sobel detector
imsobel= imgGray.sobel()
imsobel.show()

kuns=imgGray.invert().findBlobs()[-1]
mask=kuns.getFullMask()
mask.show()

# cani edges detector
imedge= imgGray.edges()
imedge.show()

im_result= imagen+mask
im_result.save('result.png')

imgrad = imgbin.morphGradient()
gr=imgrad+imagen
gr.show()
gr.save('imagen_gradiente.png')
