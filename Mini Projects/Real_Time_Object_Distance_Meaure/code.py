import cv2
import warnings
import os
warnings.filterwarnings("ignore")
import termcolor

KNOWN_DISTANCE = 46
PERSON_WIDTH = 15
CUP_WIDTH = 3
KEYBOARD_WIDTH = 4
MOBILE_WIDTH = 3
SCISSOR_WIDTH = 3

FONTS = cv2.FONT_HERSHEY_TRIPLEX

def detect_object(object):
    classes, scores, boxes = model.detect(object,0.4,0.3)
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        cv2.rectangle(object, box,(0,0,255), 2)
        cv2.putText(object,"{}:{}".format(class_names[classid],format(score,'.2f')), (box[0], box[1]-14), FONTS,0.6,(0,255,0), 3)

        if classid ==0: #person
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        elif classid == 41: #cup
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        elif classid ==66: #keyboard
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        elif classid ==67: #cell phone
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        elif classid ==76: #scissors
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
    return data_list

def cal_distance(f,W,w):
    return (W * f) / w

def cal_focalLength(d, W, w):
    return (w * d) / W

class_names = []
with open("classes.txt", "r") as objects_file:
    class_names = [e_g.strip() for e_g in objects_file.readlines()]

#download tiny.weights and .cfg here: https://github.com/lucifertrj/Yolo_Object_Detection
yoloNet = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

model = cv2.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

person_image_path = os.path.join("assets","person.jpg")
cup_image_path = os.path.join("assets","cup.jpg")
kb_image_path = os.path.join("assets","keyboard.jpg")
moblie_image_path = os.path.join("assets","mobile.jpg")
scissors_image_path = os.path.join("assets","scissors.jpg")


person_data = detect_object(cv2.imread(person_image_path))
person_width_in_rf = person_data[0][1]

keyboard_data = detect_object(cv2.imread(kb_image_path))
#print(keyboard_data)
keyboard_width_in_rf = keyboard_data[1][1]

mobile_data = detect_object(cv2.imread(moblie_image_path))
#print(mobile_data)
mobile_width_in_rf = mobile_data[1][1]

scissor_data = detect_object(cv2.imread(scissors_image_path))
#print(scissor_data)
scissor_width_in_rf = scissor_data[0][1]

cup_data = detect_object(cv2.imread(cup_image_path))
#print(cup_data)
cup_width_in_rf = cup_data[1][1]


focal_person = cal_focalLength(KNOWN_DISTANCE, PERSON_WIDTH, person_width_in_rf)
focal_cup = cal_focalLength(KNOWN_DISTANCE, CUP_WIDTH, cup_width_in_rf)
#focal_kb = cal_focalLength(KNOWN_DISTANCE, KEYBOARD_WIDTH, keyboard_width_in_rf)
focal_mobile = cal_focalLength(KNOWN_DISTANCE, MOBILE_WIDTH, mobile_width_in_rf)
focal_scissor = cal_focalLength(KNOWN_DISTANCE, SCISSOR_WIDTH, scissor_width_in_rf)

try:
    capture = cv2.VideoCapture(2)
    while True:
        _,frame = capture.read()

        data = detect_object(frame) 
        for d in data:
            print(d)
            if d[0] =='person':
                distance = cal_distance(focal_person, PERSON_WIDTH, d[1])
                x,y = d[2]
            elif d[0] =='cup':
                distance = cal_distance(focal_cup, CUP_WIDTH, d[1])
                x, y = d[2]  
            elif d[0] =='cell phone':
                distance = cal_distance(focal_mobile, MOBILE_WIDTH, d[1])
                x, y = d[2]
            elif d[0] =='scissors':
                distance = cal_distance(focal_scissor, SCISSOR_WIDTH, d[1])
                x, y = d[2]

            cv2.rectangle(frame, (x,y-3), (x+150, y+23),(255,255,255),-1)
            cv2.putText(frame,f"Distance:{format(distance,'.2f')}inchs", (x+5,y+13), FONTS, 0.45,(255,0,0), 2)
            
            print("Distance of {} is {} inchs".format(d[0],distance))

        cv2.imshow('frame',frame)
        exit_key_press = cv2.waitKey(1)

        if exit_key_press == ord('q'):
            break

    capture.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except cv2.error:
    termcolor.cprint("Select the WebCam or Camera index properly, in my case it is 2","red")
