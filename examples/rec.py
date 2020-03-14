import seetaface
try:
    import cv2
    import numpy as np
except ImportError:
    raise ImportError('opencv can not be found!')

single = 'example/single.jpg'
double = 'example/double.jpg'

fd = seetaface.FaceDetector('models/fd_2_00.dat')
fl = seetaface.FaceLandmarker('models/pd_2_00_pts81.dat')
fr = seetaface.FaceRecognizer('models/fr_2_10.dat')

def resize(image,W=400.):
    _, width, _ = image.shape
    imgScale = W/width
    newX,newY = image.shape[1]*imgScale, image.shape[0]*imgScale
    return cv2.resize(image,(int(newX),int(newY)))

def extract_features(image,rect):
    points = fl.detect(image, rect)
    return fr.extract(image,points)

def mark(mat,rect,colr):
    cv2.rectangle(mat, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), colr, 2)
    return mat

def show(mat):
    resized = resize(mat)
    cv2.imwrite('double_result.jpg', resized)
    cv2.imshow('recognition', resized)
    cv2.waitKey(0)

def test_simple():
    img = cv2.imread(single); seetaImg = seetaface.SeetaImage(img)
    faces = fd.detect(seetaImg)
    features = extract_features(seetaImg,faces[0].pos)

    img_B = cv2.imread(double); seeta_B = seetaface.SeetaImage(img_B)
    faces_B = fd.detect(seeta_B)
    
    for face in faces_B:
        rect = face.pos
        feats = extract_features(seeta_B, rect)
        sim = fr.calcsim(features,feats)
        print(sim)
        colr = (0,0,255) if sim < 0.65 else (255,0,0) 
        mark(img_B,rect,colr)

    show(img_B)

############################################################

import os

def test_database(img_path,db_path):
    if not os.path.isfile(img_path) or not os.path.isdir(db_path): 
        print("indicated path doesn't exist!");return

    # load test image
    img_A = cv2.imread(img_path); seeta_A = seetaface.SeetaImage(img_A)
    faces_A = fd.detect(seeta_A)
    featA = extract_features(seeta_A,faces_A[0].pos)
    # load database
    for fn in os.listdir(db_path):
        fp = os.path.join(db_path,fn)
        if not os.path.isfile(fp): continue
        img_B = cv2.imread(fp)
        seeta_B = seetaface.SeetaImage(img_B)
        # detect face in image
        faces_B = fd.detect(seeta_B)
        if len(faces_A) and len(faces_B):
            sim_list = []
            for face in faces_B:
                featB = extract_features(seeta_A,face.pos)
                sim = fr.calcsim(featA, featB)
                sim_list.append(sim)
                colr = (0,0,255) if sim < 0.65 else (255,0,0) 
                mark(img_B,face.pos,colr)
            print('sim: {}'.format(sim_list))
            show(img_B)

if __name__ == '__main__':
    test_simple()

    # imgpath = raw_input("test image path: ")
    # dbpath = raw_input("database path:")
    # path = "/media/ubuntu/Investigation/DataSet/Image/Face"
    # imgpath = path + "/sample.jpg"
    # dbpath = path+'/db'
    # test_database(imgpath,dbpath)