import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#User input file selection
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
img = mpimg.imread(filename)

#Preview of loaded selected image
imgplot = plt.imshow(img)
plt.show()

#Determining the dimensions of the pixel art
s = img.shape
s = np.asarray(s)
colorDimension = np.arange(0,s[2])
shortSide = np.amin([s[0],s[1]],axis = 0)
scaleFactor = shortSide/20 #This value determines the number of pixels in the smallest dimension
sp = (int(round(s[0]/scaleFactor)),int(round(s[1]/scaleFactor)))

#Central pixels to sample from in the original image
yy = np.arange(1,sp[0])*scaleFactor
ind = -1
for i in yy:
    ind += 1
    yy[ind] = int(round(i))

xx = np.arange(1,sp[1])*scaleFactor
ind = -1
for i in xx:
    ind += 1
    xx[ind] = int(round(i))

#Generating empty pixel art image
sp = (len(yy),len(xx),4)
pix = np.zeros(sp)

#Width of pixels to sample in original image
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

imgplot = plt.imshow(pix)
plt.show()
