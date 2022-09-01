import os
import shutil


def inter(a, b):
    return list(set(a) & set(b))


root = 'D:\\data'
filename_list = os.listdir(root)
target_root = 'D;\\test'

f = open('D:\\data\\test.txt')
txt = []
for line in f:
    model_data = line.split(' ')
    jpg = model_data[0].split('/')
    txt.append(jpg[1])

intersection = inter(txt, filename_list)

if not os.path.exists(target_root):
    os.makedirs(target_root)

for image_mame in intersection:
    shutil.copy(os.path.join(root, image_mame), os.path.join(target_root, image_mame))
