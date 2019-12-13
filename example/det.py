import seetaface
import cv2

root = 'example/example1.jpg'


fd = seetaface.FaceDetector('models/fd_2_00.dat')

im = cv2.imread(root)
image = seetaface.SeetaImage(im)
# or you can pass image path to SeetaImage
#  image = seetaface.SeetaImage(root)

faces = fd.detect(image)
for face in faces:
    rect = face.pos
    cv2.rectangle(im, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), (0,0,255), 2)

cv2.imwrite('example1_result.jpg', im)
cv2.imshow('win', im)
cv2.waitKey(0)
