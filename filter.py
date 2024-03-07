import cv2
import numpy as np
import scipy
import matplotlib.pyplot as plt

from scipy.interpolate import UnivariateSpline
def LookupTable(x, y):
  spline = UnivariateSpline(x, y)
  return spline(range(256))

#Read the image
image = cv2.imread('avatar.JPG')

def sharpen(image):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def HDR(img):
    hdr = cv2.detailEnhance(img, sigma_s=6, sigma_r=0.15)
    return hdr

def Summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum= cv2.merge((blue_channel, green_channel, red_channel ))
    return sum

def Winter(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win= cv2.merge((blue_channel, green_channel, red_channel))
    return win


#all image functions
sharp = sharpen(image)
highDef = HDR(image)
warm = Summer(image)
cold = Winter(image)


#list of all images
filtered_images = [sharp, highDef, warm, cold]
title = ['sharp', 'highDef', 'cold', 'warm']

#show all the filters
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(title[i])
    plt.imshow(filtered_images[i])
    plt.xticks([])
    plt.yticks([])

plt.show()