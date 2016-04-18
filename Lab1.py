#! /usr/bin/env python

from SimpleCV import Image, Camera, Display, Image
import time

cam = Camera()
img = cam.getImage()
img.save("Cartmanloco.jpg")

time.sleep(2)


