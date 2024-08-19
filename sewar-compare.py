import lpips
import os
import cv2
from sewar.full_ref import ssim, psnr

use_gpu = True
spatial = True
loss_fn = lpips.LPIPS(net='alex', spatial=spatial)

if(use_gpu):
    loss_fn.cuda()

dummy_im0 = lpips.im2tensor(lpips.load_image('datasets/validation/763.jpg'))
dummy_im1 = lpips.im2tensor(lpips.load_image('datasets/validation/763_motion3.jpg'))
if (use_gpu):
    dummy_im0 = dummy_im0.cuda()
    dummy_im1 = dummy_im1.cuda()

dist = loss_fn.forward(dummy_im0, dummy_im1)

image0 = cv2.imread('datasets/validation/763.jpg')
image1 = cv2.imread('datasets/validation/763_motion3.jpg')
print('psnr:',psnr(image0, image1))
print('ssim:',ssim(image0, image1))
print('lpips:' , dist.mean())