# check opencv version
import cv2
import os

# example of face detection with opencv cascade classifier
from cv2 import imread
from cv2 import CascadeClassifier
# load the photograph
# load the pre-trained model
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
# perform face detection
path= "C:/Python/Python35/Projects/Face detect cascade/"
for filePath in sorted(os.listdir(path)):
                fileExt = os.path.splitext(filePath)[1]
                if fileExt in [".jpg", ".jpeg",".png"]:
                        imagePath = os.path.join(path, filePath)
                        pixels = cv2.imread(imagePath);                        
                        bboxes = classifier.detectMultiScale(pixels)
                        # print bounding box for each detected face
                        for box in bboxes:
                                # extract
                                x, y, width, height = box
                                x2, y2 = x + width, y + height
                                # draw a rectangle over the pixels
                                cv2.rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
                        # show the image
                        cv2.imshow('face detection', pixels)
                        # keep the window open until we press a key
                        cv2.waitKey(0)
                        # close the window
                        cv2.destroyAllWindows()
