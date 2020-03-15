import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import subprocess
import pickle

cap = cv2.VideoCapture('gen_shit.mp4')
count = 0

n_components = 4
pca_cnt = 0
no_frames = 16

width = 480
height = 360
img_cnt = 0
enc_matrix = np.zeros((height, width, n_components))


while(True):
    ret, frame = cap.read()
    if frame is None:
        break  
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # enc_matrix[:, :, count] = gray
    count+=1

    if count == n_components:
        pca = None
        with open(f'pca-{pca_cnt}', 'rb') as f:
            pca = pickle.load(f)
        if pca is None:
            print("WHY THE FUCK!!!")
        pca_cnt+=1
        gen_matrix = pca.inverse_transform(enc_matrix)
        gen_matrix = gen_matrix.reshape((height, width, no_frames))
        for i in range(no_frames):
            cv2.imwrite(f'dec-{img_cnt}.png', gen_matrix[:, :, i])
            img_cnt += 1
        count = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

subprocess.run(["ffmpeg", "-i", "dec-%d.png", "-vcodec", "mpeg4", "gen.mp4"])

for i in range(img_cnt):
    subprocess.run(['rm', f'dec-{i}.png'])
for i in range(pca_cnt):
    subprocess.run(['rm', f'pca-{i}'])
