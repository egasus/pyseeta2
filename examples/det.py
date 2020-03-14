import seetaface
import cv2

root = 'example/example1.jpg'


fd = seetaface.FaceDetector('models/fd_2_00.dat')
fl = seetaface.FaceLandmarker('models/pd_2_00_pts81.dat')
print("model loaded")
im = cv2.imread(root)
image = seetaface.SeetaImage(im)
print("image loaded")
# or you can pass image path to SeetaImage
#  image = seetaface.SeetaImage(root)

faces = fd.detect(image)
for face in faces:
    rect = face.pos
    cv2.rectangle(im, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), (0,0,255), 2)
    points = fl.detect(image, rect)
    for p in points:
        cv2.circle(im, (int(p.x), int(p.y)), 2, (0,0,255), -1)

cv2.imwrite('example1_result.jpg', im)
cv2.imshow('win', im)
cv2.waitKey(0)
