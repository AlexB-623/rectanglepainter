import numpy as np
from PIL import Image

#create 3d Numpy array of 0s
data = np.zeros((5, 5, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

#make a red patch
data[1:4, 1:4] = [255, 0, 0]
#add a blue patch
data[2:3, 2:3] = [0, 0, 255]
#generate image
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')