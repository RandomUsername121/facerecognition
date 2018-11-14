import cv2
path0 = "C:\\Users\\Samsung\\facerecognition\\Data\\Tetris_blocks.png"
def load_and_display_image(path):
    img = cv2.imread(path, 1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
load_and_display_image(path0)
