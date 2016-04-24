#! /usr/bin/env python

from SimpleCV import Image, Camera, Display, Image
import time
import matplotlib.pyplot as plt

cam = Camera()
img = cam.getImage()
img.save("cart.jpg")


imc = Image('cart.jpg')
imcGray = imc.grayscale()
imcGray.save('cartgris.jpg')

hist = imcGray.histogram(255)
plt.figure()
plt.stem(hist)
plt.axis('tight')


time.sleep(2)


