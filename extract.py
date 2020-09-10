import os
import shutil
import torch
from IPython.display import Image, clear_output  # to display images
import cv2
import tqdm
import numpy as np
import glob
import numpy as np
import pandas as pd

def detect():
    vidcap = cv2.VideoCapture('video/HD CCTV Traffic.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("converted/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1

    #os.chdir("yolov5")
    os.system('python detect.py --weights last_yolov5s_results2.pt --img 416 --conf 0.4 --source converted')

    list_frames = pd.DataFrame(columns=['Path','Number'])

    list_frames['Number'] = list_frames['Path'].apply(lambda x: x.split('frame')[1].split('.')[0]).astype('int')

    list_frames = list_frames.sort_values('Number').reset_index(drop = True)

    img_array = []

    for filename in list_frames['Path']:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


    out = cv2.VideoWriter('Extracted/project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25,size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    owd = os.getcwd()
    os.chdir(owd)

    shutil.copy('yolov5/Extracted/project.avi', 'static/Extracted/project.mp4')