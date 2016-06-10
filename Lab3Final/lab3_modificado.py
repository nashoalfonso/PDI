from SimpleCV import Image, Camera, Display, Image, Color
import time
import matplotlib.pyplot as plt

#cam = Camera()
#img = cam.getImage()
#img.save('lunar.png')
#time.sleep(4)
#img.show()
img=Image('fotos/lunar01.png')

imgGray = img.grayscale()
imgGray.save('lunar_gris.png')

[red, green, blue]=img.splitChannels(False)

grayhist= imgGray.histogram(255)
redhist= red.histogram(255)
greenhist= green.histogram(255)
bluehist= blue.histogram(255)

plt.figure(1)
plt.subplot(221)
plt.stem(redhist);plt.title('Gray histogram');plt.axis('tight')
plt.subplot(222)
plt.stem(redhist);plt.title('Red histogram');plt.axis('tight')
plt.subplot(223)
plt.stem(greenhist);plt.title('Green histogram');plt.axis('tight')
plt.subplot(224)
plt.stem(bluehist);plt.title('Blue histogram');plt.axis('tight')
plt.savefig('fotos/histogramas.png')

red.save('fotos/lunar_en_rojo.png')
green.save('fotos/lunar_en_verde.png')
blue.save('fotos/lunar_en_azul.png')
 
imagen=Image("fotos/lunar01.png")
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
