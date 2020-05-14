import face_recognition
import cv2
from PIL import Image
from django.conf import settings
# from django.contrib.auth.models import User

def check(user):
    cam = cv2.VideoCapture(0)
    if not cam:
        return False
    cv2.namedWindow("cam-test")
    s,img = cam.read()
    i=50
    while(i>=0):
        s,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("cam-test",gray)
        i-=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    # cam.open(0)
    cv2.destroyAllWindows()
    # while True:
    #     cv2.waitKey(1)
    
    if s:
        
        # cv2.imshow("cam-test",img)
        # cv2.waitKey(2000)
        # cv2.destroyWindow("cam-test")
        cv2.imwrite("filename.jpg",img)
        url = str(settings.BASE_DIR)+user.profile.image.url
        face_1_image = face_recognition.load_image_file(url)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
        small_frame = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        check = face_recognition.compare_faces(face_1_face_encoding, face_encodings)

        # t,r,b,l = (face_recognition.face_locations(img))
        cam.release()
        print(check)
        if check[0]:
            return True
        else:
            return False
