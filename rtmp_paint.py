"""
rtmp_paint.py

User can draw shapes on the live RTMP stream with their mouse,
then quit by hitting 'Q' key

"""

import cv2

drawing = False
ix, iy = -1, -1

rectangles = []
circles = []

def callback_draw(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        return
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangles.append((ix,iy,x,y))
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        circles.append((x,y))

stream_addr = 'rtmp://s3b78u0kbtx79q.cloudfront.net/cfx/st/honda_accord'
cap = cv2.VideoCapture(stream_addr)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', callback_draw)

while(True):
    ret, frame = cap.read()
    for r in rectangles:
        cv2.rectangle(frame,(r[0],r[1]),(r[2],r[3]),(0,255,0),-1)
    for c in circles:
        cv2.circle(frame,(r[0],r[1]),5,(0,0,255),-1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
