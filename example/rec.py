import seetaface
try:
    import cv2
    import numpy as np
except ImportError:
    raise ImportError('opencv can not be found!')

root = 'example/example1.jpg'


fd = seetaface.FaceDetector('models/fd_2_00.dat')
fl = seetaface.FaceLandmarker('models/pd_2_00_pts81.dat')
fr = seetaface.FaceRecognizer('models/fr_2_10.dat')

def test_simple():
    im = cv2.imread(root)
    image = seetaface.SeetaImage(im)
    # or you can pass image path to SeetaImage
    #  image = seetaface.SeetaImage(root)

    faces = fd.detect(image)

    for face in faces:
        rect = face.pos
        cv2.rectangle(im, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), (0,0,255), 2)
        points = fl.detect(image, rect)
        for p in points:
            cv2.circle(im, (int(p.x), int(p.y)), 2, (0,0,255), -1)
        features = fr.extract(image,points)
        print(fr.calcsim(features,features))

    cv2.imwrite('example1_result.jpg', im)
    cv2.imshow('win', im)
    cv2.waitKey(0)
############################################################
def resize(image,W=400.):
    _, width, _ = image.shape
    imgScale = W/width
    newX,newY = image.shape[1]*imgScale, image.shape[0]*imgScale
    return cv2.resize(image,(int(newX),int(newY)))

import os

def test_recognition(img_path,db_path):
    if not os.path.isfile(img_path) or not os.path.isdir(db_path): 
        print("indicated path doesn't exist!");return

    # load model
    detector = fd
    aligner = fl
    identifier = fr

    # load test image
    img_A = cv2.imread(img_path)
    seeta_A = seetaface.SeetaImage(img_A)
    faces_A = detector.detect(seeta_A)

    # load database
    for fn in os.listdir(db_path):
        fp = os.path.join(db_path,fn)
        if not os.path.isfile(fp): continue
        img_B = cv2.imread(fp)
        seeta_B = seetaface.SeetaImage(img_B)
        # detect face in image
        faces_B = detector.detect(seeta_B)
        if len(faces_A) and len(faces_B):
            points_A = aligner.detect(seeta_A, faces_A[0].pos)
            featA = identifier.extract(seeta_A, points_A)
            # cv2.rectangle(image_color_A, (faces_A[0].left, faces_A[0].top), (faces_A[0].right, faces_A[0].bottom), (0,255,0), thickness=2)
            sim_list = []
            for face in faces_B:
                points_B = aligner.detect(seeta_B, face.pos)
                featB = identifier.extract(seeta_B, points_B)
                sim = identifier.calcsim(featA, featB)
                sim_list.append(sim)
            print('sim: {}'.format(sim_list))
            index = np.argmax(sim_list)
            for i, face in enumerate(faces_B):
                color = (0,255,0) if i == index else (0,0,255)
                cv2.rectangle(img_B, (face.pos.x, face.pos.y), (face.pos.x+face.pos.width, face.pos.y+face.pos.height), color, thickness=2)
            # cv2.imshow('test', resize(image_color_A))
            cv2.imshow('double', resize(img_B))
            cv2.waitKey(0)

if __name__ == '__main__':
    # imgpath = raw_input("test image path: ")
    # dbpath = raw_input("database path:")
    path = "/media/ubuntu/Investigation/DataSet/Image/Face"
    imgpath = path + "/kjy.jpg"
    dbpath = path + "/db"
    test_recognition(imgpath,dbpath)
