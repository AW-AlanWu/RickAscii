import cv2
import os
import time

cam = cv2.VideoCapture("/Users/wangkaiyu/Desktop/rickroll/resources/rickroll.mkv")

try:
    if not os.path.exists('/Users/wangkaiyu/Desktop/rickroll/image'):
        os.makedirs('/Users/wangkaiyu/Desktop/rickroll/image')

except OSError:
    print('Error: Creating directory of image')

currentframe = 0

while (True):
    ret, frame = cam.read()
    if ret:
        name = '/Users/wangkaiyu/Desktop/rickroll/image/' + str(currentframe).zfill(4) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
cam.release()
cv2.destroyAllWindows()
