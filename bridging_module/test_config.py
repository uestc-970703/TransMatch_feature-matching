import os
testset_root = './datasets/interpolation'
test_size = (1120, 780)
test_crop_size = test_size

mean = [0.429, 0.431, 0.397]
std  = [1, 1, 1]

inter_frames = 3


model = 'Bridging'
pwc_path = './utils/vfi-checkpoint.pt'


store_path = 'outputs/gastroscopy/'
checkpoint = 'qvi_release/model.pt'

