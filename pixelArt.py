import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from tkinter.filedialog import askopenfilename
filename = askopenfilename()
img = mpimg.imread(filename)

#img = mpimg.imread('C:\code\Capture.png')
imgplot = plt.imshow(img)
plt.show()

s = img.shape
s = np.asarray(s)
colorDimension = np.arange(0,s[2])
print(colorDimension)

shortSide = np.amin([s[0],s[1]],axis = 0)
scaleFactor = shortSide/20
print(scaleFactor)

sp = (int(round(s[0]/scaleFactor)),int(round(s[1]/scaleFactor)))

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

sp = (len(yy),len(xx),4)

pix = np.zeros(sp)
w = np.floor(scaleFactor)
print(w)

i = -1
while i <= len(yy)-2:
    i += 1
    j = -1
    while j <= len(xx)-2:
	    j += 1
	    for n in colorDimension:
	        pix[i,j,int(n)] = np.average(img[int(yy[i]-w):int(yy[i]+w),int(xx[j]-w):int(xx[j]+w),int(n)])
	   

print(np.shape(pix))
imgplot = plt.imshow(pix)
plt.show()
