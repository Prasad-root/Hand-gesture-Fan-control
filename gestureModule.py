import cv2
import mediapipe as mp
import math

class Gesture:
    point_x = 0
    point_y = 0

    cordinate_array = {
        # Capture points of hands
        "0":[0,0],"1":[0,0],"2":[0,0],"3":[0,0],"4":[0,0],
        "5":[0,0],"6":[0,0],"7":[0,0],"8":[0,0],"9":[0,0],
        "10":[0,0],"11":[0,0],"12":[0,0],"13":[0,0],"14":[0,0],
        "15":[0,0],"16":[0,0],"17":[0,0],"18":[0,0],"19":[0,0],
        "20":[0,0]}
    
    def __init__(self,static_image=False,handCount=1,min_detection_confidence=0.5,track_confidence = 0.5):
        self.static_image = static_image
        self.handCount = handCount
        self.min_detection_confidence = min_detection_confidence
        self.track_confidence = track_confidence

        self.mpObj = mp.solutions.hands
        self.hand = self.mpObj.Hands(self.static_image,self.handCount)
        self.mpDrawing = mp.solutions.drawing_utils

    
    def handDetect(self,frame,status = True):
        self.rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.result_img = self.hand.process(self.rgb_frame) # Process Hand gesture Functionality in conterted Images
        if self.result_img.multi_hand_landmarks:
            for detectedHands in self.result_img.multi_hand_landmarks:
                self.mpDrawing.draw_landmarks(frame,detectedHands) #  self.mpObj.HAND_CONNECTIONS
        return self.result_img


    def collectPointCodinates(self,printing=False): 
        if self.result_img.multi_hand_landmarks:     
            height,width,c = self.rgb_frame.shape

            gesture_Hand = self.result_img.multi_hand_landmarks[0]
            for id,lm in enumerate(gesture_Hand.landmark):
                if printing:
                    print(f"{id} x: {(lm.x*width)} | y:{lm.y*height}")

                point_x = int(lm.x*width)
                point_y = int(lm.y*height)
                self.cordinate_array[str(id)] = [point_x,point_y]
        return self.cordinate_array
    
    def stackTip2Base(self, image,codinates,hand_controlling_finger_pair,makers=False):
        
        if self.result_img.multi_hand_landmarks:
            #self.collectPointCodinates() # Detect Hand Point cordinates

            colorCode = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255),(100, 150, 255)]

            for finger_pair, color in zip(hand_controlling_finger_pair, colorCode):
                tip_cordinates_x = codinates[str(finger_pair[0])][0]
                tip_cordinates_y = codinates[str(finger_pair[0])][1]

                base_cordinates_x = codinates[str(finger_pair[1])][0]
                base_cordinates_y = codinates[str(finger_pair[1])][1]
                
                if makers:
                    cv2.circle(image, (tip_cordinates_x, tip_cordinates_y), 5, color, 5)
                    cv2.circle(image, (base_cordinates_x, base_cordinates_y), 5, color, 5)
                    cv2.line(image, (tip_cordinates_x, tip_cordinates_y), (base_cordinates_x, base_cordinates_y), color, 5)

    def distance_calculate_2points(self,pair_of_points): 
        output = []       
        for first_point,second_point in pair_of_points:
            first_point_x,first_point_y = self.cordinate_array[str(first_point)]
            second_point_x,second_point_y = self.cordinate_array[str(second_point)]
            output.append([int(math.hypot(second_point_x-first_point_x,second_point_y-first_point_y))])
        return output
    