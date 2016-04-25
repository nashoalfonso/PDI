#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
figure(1)
img.show()

imgGray = img.grayscale()
figure(2)
imgGray.show()

# aqui hay que elegir entre estas 2 opciones

# Opcion 1: histograma sobre escala de grises

hist = imgGray.histogram(255)		# histograma de lo3 colores juntos
plot(hist)
