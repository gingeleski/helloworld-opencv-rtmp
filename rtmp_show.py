"""
rtmp_show.py

Just shows RTMP stream from given address, until user hits 'Q' key

"""

import cv2

stream_addr = 'rtmp://s3b78u0kbtx79q.cloudfront.net/cfx/st/honda_accord'
cap = cv2.VideoCapture(stream_addr)
 
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
