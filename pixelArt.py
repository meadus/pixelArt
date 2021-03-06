#Game boy like pixel art generator, downscales image to a desired size and applies a game boy color palette

#Required packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#User input file selection, a PNG image should be selected.
from tkinter.filedialog import askopenfilename
from tkinter import *
root = Tk()
filename = askopenfilename(title = "Select Image", filetypes = (("png files","*.png"),("all files","*.*")))
img = mpimg.imread(filename)
root.destroy()

#What size do you want the short edge of the pixel art?
pixelArtShortSide = float(input("Pixel art short edge size (original Game Boy Classic resolution was 160 x 144):"))


#Determining the dimensions of the pixel art (downscaling)
s = img.shape
s = np.asarray(s)
colorDimension = np.arange(0,s[2])
shortSide = np.amin([s[0],s[1]],axis = 0)
scaleFactor = shortSide/pixelArtShortSide
sp = (int(round(s[0]/scaleFactor)),int(round(s[1]/scaleFactor))) #Final array size

#Central pixels to sample from in the original image
yy = np.arange(1,sp[0])*scaleFactor
ind = -1
for i in yy:
    ind += 1
    yy[ind] = int(round(i)) #y indices to be sampled

xx = np.arange(1,sp[1])*scaleFactor
ind = -1
for i in xx:
    ind += 1
    xx[ind] = int(round(i)) #x indices to be sampled

#Generating empty pixel art image
sp = (len(yy),len(xx),len(colorDimension))
pix = np.zeros(sp)

#Number of pixels wide to sample in original image
w = np.floor(scaleFactor)

#Sampling process
i = -1
while i <= len(yy)-2:
    i += 1
    j = -1
    while j <= len(xx)-2:
	    j += 1
	    for n in colorDimension: #Varies depending on image type
	        pix[i,j,int(n)] = np.average(img[int(yy[i]-w):int(yy[i]+w),int(xx[j]-w):int(xx[j]+w),int(n)])

#Setting up the color palette to be applied
rgb = np.arange(0,3)
gameBoy = np.array([[15,56,15],[48,98,48],[139,172,15],[155,188,15]]) #original gameboy four colour palette
gameBoy = gameBoy/255
colorMapDim = np.shape(gameBoy)
gbPix = np.zeros(sp) #new images with adjusted colours

#Iterating through the "pixelized" image and applying the proper color
i = -1
while i <= len(yy)-2:
    i += 1
    j = -1
    while j <= len(xx)-2:
        j += 1
        err = np.zeros(colorMapDim)
        for k in rgb:
            err[0:,k] = gameBoy[0:,k] - pix[i,j,k]
        err = np.power(err,2)
        err = np.sum(err, axis = 1) #Results in a squared error for each pixel vs. the colour palette
        colorCode = np.where(err == np.min(err))
        gbPix[i,j,0:3] = gameBoy[colorCode,0:] #The closest colour in the palette (minimum squared error) is assigned to the new array

#Exporting the new image to the local folder
mpimg.imsave("art.png",gbPix)
