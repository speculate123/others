import cv2

cap = cv2.VideoCapture(r'C:\Users\yt335\pytorch-YOLOv4\data\hightway.mp4')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
length
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))

ret, img = cap.read()
while (ret):
    out.write(img)
    ret, img = cap.read()
