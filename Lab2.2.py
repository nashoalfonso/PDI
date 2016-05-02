#! /usr/bin/env python

from SimpleCV import Image, Camera, Display, Image
import time
import matplotlib.pyplot as plt

cam = Camera()
img = cam.getImage()
img.save('hola.png')
img.show()
time.sleep(4)

imgb = img.binarize()
imgb.save('hola_bin.png')
imgb.show()

imgGray = img.grayscale()
imgGray.show()
imgGray.save('hola_gris.png')

hist = imgGray.histogram(255)
plt.figure(1)
plt.stem(hist)
plt.axis('tight')
plt.title('Escala de grises')
plt.savefig('histgris.png')
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

#plt.subplot(312)
plt.figure(3)
plt.stem(green_hist)
plt.title('Green histogram')
plt.axis('tight')
plt.savefig('hist(green).png')

plt.figure(4)
#plt.subplot(313)
plt.stem(blue_hist)
plt.title('Blue histogram')
plt.axis('tight')
plt.savefig('hist(blue).png')

peaks = img.huePeaks()
print peaks
peak_1 = peaks[0][0]
#peak_2 = peaks[1][1]
ue = img.hueDistance(peak_1)
ue.save('ue.png')
#ue2 = img.hueDistance(peak_2)
#ue2.save('ue2.png')
