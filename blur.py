import cv2
import matplotlib.pyplot as plt

img = cv2.imread('avatar.JPG')
cv2.imshow('Image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

box = cv2.boxFilter(img, -1, (25, 25))
blur = cv2.blur(img, (15, 15))
gaussian = cv2.GaussianBlur(img, (17, 17), 0)
median = cv2.medianBlur(img, ksize=5)

images = [box, blur, gaussian, median]
title =  ['box', 'blur', 'gaussian', 'median']

# blurrings in cv2
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(title[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
