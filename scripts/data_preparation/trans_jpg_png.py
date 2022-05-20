import PIL.Image
import os
i = 0
path = "datasets/train_HR_sub_jpg/"
savepath = "datasets/train_HR_sub/"
filelist = os.listdir(path)
for file in filelist:
    im = PIL.Image.open(path+filelist[i])
    filename = os.path.splitext(file)[0]
    im.save(savepath+filename+'.png') # or 'test.tif'
    i=i+1