import numpy as np
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb
import matplotlib.pylab as plt


# 约束S
def bound1(R,G,B):
	# 如果sum的元素为0 将其置为min对应的元素
	sum = R+G+B 
	min = 3*np.minimum(np.minimum(R,G),B)
	sum1 = np.where(sum==0, np.finfo(np.float64).eps, sum)
	S = 1 - min/sum1
	return S

# 约束θ
def bound2(R,G,B):
	a = (2*R-G-B)/2
	b = (R-G)**2+(R-G)*(G-B)
	b1 = np.where(b<=0, np.finfo(np.float64).eps, b)
	b1 = b1**0.5
	θ = np.arccos(np.clip(a/b1,-1,1)) #clip用来约束元素
	H = np.where(B>G, 2*np.pi-θ, θ)
	H = np.where(H<0, 2*np.pi+H, H)
	H = H/(2*np.pi)
	return H

# 读取图片
im = imread('spongebob.jpg')
# 将其分为三个通道
R,G,B = im[:,:,0]/255, im[:,:,1]/255, im[:,:,2]/255
# 将三个2D数组合为一个3D数组
im1 = np.stack([R,G,B], axis=2)

# RGB转化为HSI
I = (R+G+B)/3 
S = bound1(R,G,B)
H = bound2(R,G,B)
im2 = rgb2hsv(im)

im3 = np.stack([H,S,I], axis=2)

# 显示图像
plt.figure(figsize=(10,5))
plt.subplot(221), plt.imshow(im), plt.axis('off')
plt.title('im', size=20)
plt.subplot(222), plt.imshow(im1), plt.axis('off')
plt.title('im1', size=20)
plt.subplot(223), plt.imshow(im2), plt.axis('off')
plt.title('im2', size=20)
plt.subplot(224), plt.imshow(im3), plt.axis('off')
plt.title('im3', size=20)
plt.show()


'''
[1] python中多个矩阵点对点取最大值方法 https://www.cnblogs.com/gzl0612/p/15080411.html
[2] RGB HSI HSV HSB HSL https://www.cnblogs.com/fordreamxin/p/4616861.html
[3] Conversion from RGB to HSI https://answers.opencv.org/question/62446/conversion-from-rgb-to-hsi/
[4] RGB-to-HSI and HSI-to-RGB Conversions  http://www.4hathacker.in/2015/11/rgb-to-hsi-and-hsi-to-rgb-conversions.html
[5] RGB图像转到HSI图像 http://t.csdn.cn/biFcA
[6] Smallest positive float64 number https://stackoverflow.com/questions/38477908/smallest-positive-float64-number
[7] skimage.io.imread与cv2.imread的区别 http://t.csdn.cn/19EYH

plt.imshow输入的矩阵可以为：
M,N 灰度图像
M,N,3 RGB彩色图像
M,N,4 RGBA彩色图像
显示灰度图像，需要在plt.imshow()里添加参数cmap="gray"
MxN维度的矩阵元素为0-255的整数或0-1的浮点数

np.nan_to_num( , copy=True)将inf nan置为0
'''