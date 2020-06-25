# Face-detection-projects-Cascade-VS-MTCNN
This project compares 2 face detection methods. First is the Cascade based(opencv package) and Multi-task Cascade Convolutional Neural Network, or MTCNN.


### METHOD 1 : Using OpenCV CascadeClassifier()

OpenCV's CascadeClassifier class can be used to create a cascade classifier for face detection. It takes a filename as an argument that specifies the XML file for a pre-trained model.This file is the trained cascade xml file that is trained on harr-like features by using many positive (images containing faces) and many negative(images not containing faces)  images.

Reference: 

Cascade classifier package of OpenCV: https://github.com/opencv/opencv/tree/master/data/haarcascades

For more info on cascade classifier : https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

For detailed training using cascade classifier : https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html

Here i am using already trained xml file provided by Opencv : https://github.com/opencv/opencv/tree/master/data/haarcascades

Original paper on cascade based face detector: https://d1wqtxts1xzle7.cloudfront.net/49703040/Robust_Real-Time_Face_Detection20161018-7210-40857c.pdf?1476846089=&response-content-disposition=inline%3B+filename%3DRobust_Real-Time_Face_Detection.pdf&Expires=1593067287&Signature=GvwOMJshyPiLa5icS5ePDpVmOW4kC0MDBkN-7TfxtzenFinRaItYADwW-ih3zFl59VnX0UX1MBT-Qcn3B8JcXst~EqdkK77x93waPLCz2V-QhdfV6qvCUqVOSHWiEEHePT6iTYO-aYD--0pqUDz3UavH6m3nf53AuPsk4rpzjObfJRF-Q0ZhAL3OZM8Xh4LcKP2zPphWKoKpyb1GyDMxd6G9U4BEieKrJha7zFMte0NCG4U7yNh6Ry~m8Cuj9mm~G2qG1fwocCStnWvGShdm27dMR4nJ1ZfHRMiE-4DODTRluu5JkKDuXauAKeS9ErnSB2DoeuRCOhYP0QISbC-hvA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

Steps:

1.Build a classifier using CascadeClassifier class by providing trained xml file.

2.Use detectMultiScale to detects objects of diffrent sizes and returns them as list of rectangles.

(https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale#cascadeclassifier-detectmultiscale)


3. Use opencv's cv2.rectangle to draw rectangle around detected face.


Code : cascade_face_detector.py

### METHOD 2 : Using Multi-task Cascade Convolutional Neural Network(MTCNN)

The proposed CNNs consist of three stages. In the first stage (Proposal Network or P-Net), it produces candidate windows quickly through a shallow CNN. Then, it refines the windows to reject a large number of non-faces windows through a more complex CNN(Refine Network or R-Net).  Finally, it uses a more powerful CNN(Output Network or O-Net) to refine the result and output facial landmarks positions.


Reference : 

Original paper : https://arxiv.org/ftp/arxiv/papers/1604/1604.02878.pdf

Steps:

1. Install mtccnn package (using pip)

2. Build detector using MTCNN()

3. Draw the rectangle on face detected and small circles on face features (eye, nose etc)

















