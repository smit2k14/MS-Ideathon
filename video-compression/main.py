import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

cap = cv2.VideoCapture('hello.mp4')
count = 0

no_frames = 4
vid_matrix = np.zeros((278, 500, no_frames))

n_components = 2

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
        generated_frames = pca.inverse_transform(transformed_frames)


        #generated_frames[:, i] is the generated image frame by frame and vid_matrix is the orginal image
        for i in range(no_frames):
            
            plt.figure(1)
            plt.imshow(generated_frames[:, i].reshape(278, 500))
            plt.title('Recreated')
            plt.show()
            plt.figure(2)
            plt.imshow(vid_matrix[:, :, i].reshape(278, 500))
            plt.title('Original')
            plt.show()
        
        count = 0


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()