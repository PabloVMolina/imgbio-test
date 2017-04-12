import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return rgb[...,:3] @ [0.299, 0.587, 0.114]

img = plt.imread("Lenna.png",1)
print(img.shape)

plt.set_cmap('gray')
plt.imshow(img)
plt.show()
