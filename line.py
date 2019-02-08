#line.py
#Por Luis Diego Fernandez
#v-1.20.20

import sys
import math
import time
import bmp_maker

# image attributes
width = 400
height = 400
x_point_1 = 1
y_point_1 = 1
x_point_2 = 1
y_point_2 = 1
bits_per_pixel = 32

print("BMP image maker V-2\n")

if(len(sys.argv) != 7):
	print("Incorrect number of arguments entered")
	print("Enter the necessary arguments: width lenght x_point_1 y_point_1 x_point_2 y_point_2")
	sys.exit()
try:
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	x_point_1 = float(sys.argv[3])
	y_point_1 = float(sys.argv[4])
	x_point_2 = float(sys.argv[5])
	y_point_2 = float(sys.argv[6])

except ValueError:
	print("Use only integer numbers")
	sys.exit()


if (width < 1):
	width = 1

if (height < 1):
	height = 1

if (x_point_1 < -1 or x_point_1 > 1 or y_point_1 < -1 or y_point_1 > 1):
	print("The point 1 is out of range")

if (x_point_2 < -1 or x_point_2 > 1 or y_point_2 < -1 or y_point_2 > 1):
	print("The point 2 is out of range")

newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glClearColor(0,0,0)
newBmpImage.glClear()

newBmpImage.glColor(1,1,1);

newBmpImage.glLine(x_point_1,y_point_1,x_point_2,y_point_2)

newBmpImage.glFinish()

print("Done")
