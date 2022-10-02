import numpy as np
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb
import matplotlib.pylab as plt


# 读取图片
im = imread('spongebob.jpg')
# 将其分为三个通道
R,G,B = im[:,:,0]/255, im[:,:,1]/255, im[:,:,2]/255

# 用函数将RGB转化为HSV
im1 = rgb2hsv(im)

# 自己编程将RGB转化为HSV
max = np.maximum(np.maximum(R,G),B)
min = np.minimum(np.minimum(R,G),B)
V = max 
a, b = max-min+np.finfo(np.float64).eps, max+np.finfo(np.float64).eps
S = a/b
H = np.zeros([V.shape[0], V.shape[1]])
H = np.where(max == R, 60*(G-B)/a, H)
H = np.where(max == G, 120+60*(B-R)/a, H)
H = np.where(max == B, 240+60*(R-G)/a, H)
H = np.where(H<0, H+360, H)
H = H/360 #H范围为0-360° 将其归一化
im2 = np.stack([H,S,V], axis=2)

# 显示图像
plt.figure(figsize=(10,5))
plt.subplot(221), plt.imshow(im), plt.axis('off')
plt.title('im', size=20)
plt.subplot(223), plt.imshow(im1), plt.axis('off')
plt.title('im1', size=20)
plt.subplot(224), plt.imshow(im2), plt.axis('off')
plt.title('im2', size=20)
plt.show()