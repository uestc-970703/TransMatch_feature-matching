import torch
import lpips
import os
import cv2
from sewar.full_ref import ssim, psnr
use_gpu = True
spatial = True
loss_fn = lpips.LPIPS(net='alex', spatial=spatial)

if(use_gpu):
    loss_fn.cuda()

img0_list = []
img1_list = []
psnr_sum = 0
ssim_sum = 0

img0_path = './images'
img1_path = './results'
img0_images = os.listdir(img0_path)
img1_images = os.listdir(img1_path)
img0_images.sort(key=lambda x:int(x.split('.')[0]))
img1_images.sort(key=lambda x:int(x.split('.')[0]))
for img0 in img0_images:
    img_0 = os.path.join(img0_path, img0)
    img0_list.append(img_0)

for img1 in img1_images:
    img_1 = os.path.join(img1_path, img1)
    img1_list.append(img_1)

dist_list = []
for i in range(len(img0_list)):
    dummy_im0 = lpips.im2tensor(lpips.load_image(img0_list[i]))
    dummy_im1 = lpips.im2tensor(lpips.load_image(img1_list[i]))
    if (use_gpu):
        dummy_im0 = dummy_im0.cuda()
        dummy_im1 = dummy_im1.cuda()

    dist = loss_fn.forward(dummy_im0, dummy_im1)
    dist_list.append(dist.mean().item())
    print('lpips:', dist.mean())
    image0 = cv2.imread(img0_list[i])
    image1 = cv2.imread(img1_list[i])
    print('psnr:',psnr(image0, image1))
    print('ssim:',ssim(image0, image1))
    psnr_sum += psnr(image0,image1)
    ssim_sum += ssim(image0,image1)[0]
print('Average lpips: %.3f ' % (sum(dist_list)/len(img0_list)))
print('Average psnr:', psnr_sum/len(img0_list))
print('Average ssim:', ssim_sum/len(img0_list))

