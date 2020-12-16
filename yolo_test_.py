import darknet
import numpy as np
import cv2
import time
import smtplib
from email.mime.text import MIMEText

# load configure file, dataset, pre-weights
net, cn, color = darknet.load_network('yolov3-tiny.cfg', 'coco.data', 'yolov3-tiny_10000.weights')
width = darknet.network_width(net)
height = darknet.network_height(net)
darknet_image = darknet.make_image(width, height, 3)

cap = cv2.VideoCapture(0) # video capture

sendEmail = "jji1902@naver.com"
recvEmail = "jji1902@naver.com"
password = "wldus0509!"
label_name="jjy"

def send_mail(sendEmail,recvEmail,password,label_name):
    smtpName = "smtp.naver.com" #smtp 서버 주소
    smtpPort = 587 #smtp 포트 번호

    text = label_name+"님이 귀가하셨습니다."
    msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

    msg['Subject'] =label_name+"님 귀가"
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    print(msg.as_string())

    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( sendEmail , password ) #로그인
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.close() #smtp 서버 연결을 종료합니다.


print('capped!')        
prevTime = 0
fpss = []
count = 10
while(cap.isOpened()):
	ret, frame = cap.read() # read capture video frame
	if ret: # ture: read frame successed, false: read frame failed
		
		# get FPS
		curTime = time.time()
		sec = curTime - prevTime
		prevTime = curTime
		fps = 1/(sec)
		fpss.append(fps)
		avr_fps = sum(fpss)/len(fpss)
		str = "FPS : %0.1f" % avr_fps

		frame_resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LINEAR) # resize image
		frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB) # change bgr image 2 rgb image
		darknet.copy_image_from_bytes(darknet_image, frame_rgb.tobytes())
		r = darknet.detect_image(net, cn, darknet_image) # detect obj from image 
		image = darknet.draw_boxes(r, frame_resized, color) # draw box on the image
		
		#image = cv2.resize(image, (len(frame[0])/4, len(frame)/4)) 

		cv2.putText(image, str, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255)) # put fps text on image
		cv2.imshow('show',image)
		for found in r: # for all detected obj
			label_name, prob, loc = found[0], found[1], found[2] # get label name, probablility, location
			print(label_name)
			if count >10:
				send_mail(sendEmail,recvEmail,password,label_name)
				count = 0
		count = count+1
		
		k = cv2.waitKey(1)
		if k == 27:
			break
		elif k == ord('s'):
			cv2.imwrite('saved_image.png',image)
	else:
		print('No Frame')
		break
cap.release()
cv2.destroyAllWindows()
