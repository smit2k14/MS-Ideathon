import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import subprocess
import pickle

cap = cv2.VideoCapture('vid1.mp4')
count = 0

width = 480
height = 360

no_frames = 16
vid_matrix = np.zeros((height, width, no_frames))

n_components = 8
img_cnt = 0
dec_cnt = 0
pca_cnt = 0

while(True):
    ret, frame = cap.read()
    if frame is None:
        break  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vid_matrix[:, :, count] = gray
    count+=1

    if count == no_frames:
        col_vec = np.zeros((gray.shape[0] * gray.shape[1], no_frames))

        for i in range(no_frames):
            col_vec[:, i] = vid_matrix[:, :, i].reshape((gray.shape[0] * gray.shape[1]))
        pca = PCA(n_components = n_components)
        transformed_frames = pca.fit_transform(col_vec)

        with open('pca-{}'.format(pca_cnt), 'wb') as f:
            pickle.dump(pca, f)
        
        with open('pca-{}'.format(pca_cnt), 'rb') as f:
            pca = pickle.load(f)
        

        pca_cnt += 1
        generated_frames = pca.inverse_transform(transformed_frames)
        #generated_frames[:, i] is the generated image frame by frame and vid_matrix is the orginal image
        for i in range(n_components):
            cv2.imwrite(f"img-{img_cnt}.png", transformed_frames[:, i].reshape(height, width))
            img_cnt += 1
        
        for i in range(no_frames):
            cv2.imwrite(f"dec-{dec_cnt}.png", generated_frames[:, i].reshape(height, width))
            dec_cnt += 1
        

        count = 0


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

subprocess.run(["ffmpeg", "-i", "img-%d.png", "-vcodec", "mpeg4", "gen_shit1.mp4"])

for i in range(img_cnt):
    subprocess.run(['rm', f'img-{i}.png'])


subprocess.run(["ffmpeg", "-i", "dec-%d.png", "-vcodec", "mpeg4", "gen_shit2.mp4"])

for i in range(dec_cnt):
    subprocess.run(['rm', f'dec-{i}.png'])
