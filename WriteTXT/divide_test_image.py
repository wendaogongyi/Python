import os
import shutil


root = 'D:\\data'
filename_list = os.listdir(root)
target_root = 'D;\\test'

f = open('D:\\data\\test.txt')
txt = []
for line in f:
    model_data = line.split(' ')
    jpg = model_data[0].split('/')
    txt.append(jpg[1])

if not os.path.exists(target_root):
    os.makedirs(target_root)

for image_mame in txt:
    shutil.copy(os.path.join(root, image_mame), os.path.join(target_root, image_mame))
