import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("Lenna.png")
print(img.shape)

plt.imshow(img)
plt.show()
