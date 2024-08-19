import cv2 as cv
import numpy as np

img = cv.imread('noiseimage.png', 0)
h = img.shape[0]
w = img.shape[1]

img_Blur_3 = cv.blur(img, (3, 3))
img_Blur_5 = cv.blur(img, (5, 5))

img_MedianBlur_3 = cv.medianBlur(img, 3)
img_MedianBlur_5 = cv.medianBlur(img, 5)

def overrun_pixel_smoothing(kernel, image):
    img_overrun = image.copy()
    filter = np.zeros((kernel, kernel), np.uint8)
    average = np.zeros((h - kernel + 1, w - kernel + 1), np.uint8)

    for i in range(h - kernel + 1):
        for j in range(w - kernel + 1):

            for m in range(kernel):
                for n in range(kernel):
                    filter[m, n] = img_overrun[i + m, j + n]

            average[i, j] = 1 / (kernel * kernel) * filter.sum()
    T = 50

    for i in range(h - kernel + 1):
        for j in range(w - kernel + 1):

            if abs(img[i + kernel - 2, j + kernel - 2] - average[i, j]) > T:
                img_overrun[i + kernel - 2, j + kernel -2] = average[i,j]
    return img_overrun

img_overrun_3 = overrun_pixel_smoothing(3, img)
img_overrun_5 = overrun_pixel_smoothing(5, img)

img_EdgeKeeping = img.copy()
filter = np.zeros((5, 5), np.uint8)

for i in range(h - 4):
    for j in range(w - 4):

         for m in range(5):
             for n in range(5):
                 filter[m,n] = img_EdgeKeeping[i + m, j + n]

         mask = []
         mask.append([filter[1, 1], filter[1, 2], filter[1, 3], filter[2, 1], filter[2, 2], filter[2, 3], filter[3, 1], filter[3, 2], filter[3, 3]])

         mask.append([filter[2, 2], filter[1, 1], filter[1, 2], filter[1, 3], filter[0, 1], filter[0, 2], filter[0, 3]])
         mask.append([filter[2, 2], filter[1, 1], filter[2, 1], filter[3, 1], filter[1, 0], filter[2, 0], filter[3, 0]])
         mask.append([filter[2, 2], filter[3, 1], filter[3, 2], filter[3, 3], filter[4, 1], filter[4, 2], filter[4, 3]])
         mask.append([filter[2, 2], filter[1, 3], filter[2, 3], filter[3, 3], filter[1, 4], filter[2, 4], filter[3, 4]])

         mask.append([filter[2, 2], filter[3 ,2], filter[2, 3], filter[3, 3], filter[4, 3], filter[3, 4], filter[4, 4]])
         mask.append([filter[2, 2], filter[2, 3], filter[1, 2], filter[1, 3], filter[0, 1], filter[0, 2], filter[0, 3]])
         mask.append([filter[2, 2], filter[1, 2], filter[2, 1], filter[1, 1], filter[0, 1], filter[1, 0], filter[0, 0]])
         mask.append([filter[2, 2], filter[2, 1], filter[3, 2], filter[3, 1], filter[3, 0], filter[4, 1], filter[4, 0]])

         var = []
         for k in range(9):
             var.append(np.var(mask[k]))

             index = var.index(min(var))
             img_EdgeKeeping[i + 2, j + 2] = np.mean(mask[index])

cv.imshow('img_MedianBlur_3', img_MedianBlur_3)
cv.imshow('img_MedianBlur_5', img_MedianBlur_5)
cv.imshow('img_EdgeKeeping', img_EdgeKeeping)
cv.imshow('img_Blur_5',img_Blur_5)
cv.imshow('img_overrun_5',img_overrun_5)

cv.waitKey(0)
cv.destroyWindow()
