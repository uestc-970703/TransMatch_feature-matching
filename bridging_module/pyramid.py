import cv2
import numpy as np

A = cv2.imread('datasets/example/car-turn/00077.jpg')
B = cv2.imread('datasets/example/car-turn/00001.jpg')

G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(5,0,1):
    GE = cv2.pyrUp(gpA[i])
    print(i,gpA[i-1].shape, GE.shape)
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

lpB = [gpA[5]]
for i in range(5,0,1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

LS = []
for i,(la,lb) in enumerate(zip(lpA,lpB)):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2],lb[:,cols//2:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_,LS[i])

real = np.hstack((la[:, :cols//2],lb[:,cols//2:]))
cv2.imshow('ls_', ls_)
cv2.imshow('real', real)
cv2.waitKey(0)
cv2.destroyWindow()