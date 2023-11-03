import cv2
#opencv dnn
net=cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolo4-tiny.cfg")
model=cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255)
#load lists
classes=[]
with open("dnn_model/classes.txt","r")as file_object:
    for class_name in file_object.readlines():
        class_name=class_name.strip()
        classes.append(class_name)

print("OBJECT LIST")
print(classes)





#open camera
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    #get frame
    ret,frame=cap.read()
    #object detection
    (class_ids,score,bboxes)=model.detect(frame)
    for class_ids,score,bbox in zip(class_ids,score,bboxes):
        (x,y,w,h)=bbox
        class_name=classes[class_id]

        cv2.putText(frame,class_name,(x,y-5),cv2.FONT_HERSHEY_PLAIN,2,(200,0,50),2)
        
        cv2.rectangle(frame,(x,y),(x+m,y+h),(200,0,50),3)
        
    print("CLASS IDS",class_ids)
    print("scores",scores)
    print("bboxes",bboxes)
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)
