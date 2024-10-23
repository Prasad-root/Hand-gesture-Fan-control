import cv2
import mediapipe as mp
from gesture import Gesture
import time
import serial
from connection import conn


sended_message = ""


def sendmessages(data):
    global sended_message
   
    d = data
    if d != sended_message:
        #print(f"SENDED MESSAGE : {sended_message}  |  DATA  {data}")
        conn(d)
        cv2.putText(frame, f"send", (1100, 91), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
        cv2.arrowedLine(frame, (1200,85), (1200,95), (0,255,255), 8, tipLength=3)
        sended_message = data

width, height = 1600, 900  # Width and Height
ptime = 0

gesture_Hand = Gesture()

capture = cv2.VideoCapture(0)
capture.set(3, width)  # Set width for window
capture.set(4, height)  # Set height for window

hand_controlling_finger_pair = [[8, 5], [12, 9], [16, 13], [20, 17], [4, 1]]

while True:
    status, frame = capture.read()
    frame = cv2.flip(frame,1)  # Read capture 
    gesture_Hand.handDetect(frame)  # Detect Hand
    codinates = gesture_Hand.collectPointCodinates(False)
    gesture_Hand.stackTip2Base(frame, codinates, hand_controlling_finger_pair)

    output = gesture_Hand.distance_calculate_2points(hand_controlling_finger_pair)
    # print(output)

    ctime = time.time()
    fps = int(1 / (ctime - ptime))
    ptime = ctime

    cv2.putText(frame, f"FPS : {str(fps)}", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    first_finger = output[0][0]
    second_finger = output[1][0]
    third_finger = output[2][0]
    fourth_finger = output[3][0]

    first_finger_status = False
    second_finger_status = False
    third_finger_status = False
    fourth_finger_status = False

    if first_finger > 140:
        first_finger_status = True
    if second_finger > 155:
        second_finger_status = True
    if third_finger > 165:
        third_finger_status = True
    if fourth_finger > 150:
        fourth_finger_status = True

    cv2.circle(frame, (100, 150), 30, (255, 255, 0), 3)
    cv2.circle(frame, (100, 230), 30, (0, 0, 255), 3)
    cv2.circle(frame, (100, 310), 30, (255, 255, 255), 3)
    cv2.circle(frame, (100, 390), 30, (0, 255, 0), 3)

    if fourth_finger_status:
        # Turn on the fan
        cv2.circle(frame, (100, 150), 30, (255, 255, 0), -1)
        cv2.putText(frame, f"4", (92, 156), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, f"ON", (88, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        sendmessages("4")
    elif third_finger_status:
        cv2.circle(frame, (100, 230), 30, (0, 0, 255), -1)
        cv2.putText(frame, f"3", (92, 236), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, f"ON", (88, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        sendmessages("3")
    elif second_finger_status:
        cv2.circle(frame, (100, 310), 30, (255, 255, 255), -1)
        cv2.putText(frame, f"2", (92, 316), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, f"ON", (88, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        sendmessages("2")
    elif first_finger_status:
        cv2.circle(frame, (100, 390), 30, (0, 255, 0), -1)
        cv2.putText(frame, f"1", (92, 396), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, f"ON", (88, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        sendmessages("1")
    else:
        sendmessages("0")
        cv2.putText(frame, f"OFF", (88, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Web Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
