# KW-VIP-2020-2-team-project
KW VIP 2020-2 team project

## YoloV3 training 
데이터셋 : 팀원 4명의 얼굴 ( 클래스 : 4 ) 
1. cfg/yolov3-tiny.cfg 파일
--> 마지막 Convolution layer filters = 27 ( = (4+5)*3 ) 로 수정
--> yolo classes = 4 로 수정

2. cfg/coco.data 파일
--> train, valid 위치 변경 (데이터셋 저장되어있는 위치로 변경)

3. data/coco.names 파일
--> 클래스 이름 추가 (4명의 라벨 이름 추가 ex) owner , ss, jjy, Michael Kim )

4. data/img 폴더
--> 이미지(png, jpg), 이미지 어노테이션 파일(txt) 저장

5. data/train.txt, data/test.txt 파일
--> data/train.txt : train할 이미지 위치 저장한 파일
--> data/test.txt : test할 이미지 위치 저장한 파일

6. convlolution layer 
--> wget https://pjreddie.com/media/files/darknet53.conv.74

7. training 
--> ./darknet detector train cfg/coco.data cfg/yolov3-tiny.cfg darknet53.conv.74

8. test
--> ./darknet detect cfg/yolov3.cfg backup/yolov3-tiny_10000.weights data/person.jpg
