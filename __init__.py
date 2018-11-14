import cv2
import numpy as np
from matplotlib import pyplot as plt

path0 = "C:\\Users\\Proprietaire\\facerecognition\\Data\\Tetris_blocks.png"

def load_and_display_image(path):
    img = cv2.imread(path, 1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#load_and_display_image(path0)

def edges(filepath):
    img = cv2.imread(filepath,1)
    edges = cv2.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

edges(path0)


def process_image2(path):
    img = cv2.imread(path,1)
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

process_image2(path0)
