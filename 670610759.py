#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

showfinger = []
Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    showfinger.clear()

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)               
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy 
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy      
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy                                     
            if cx4 < cx3:
                pong = 0 
                if "Thumb" in showfinger:
                    showfinger.remove("Thumb")                   
            else:
                pong = 1
                if "Thumb" not in showfinger:
                    showfinger.append("Thumb")
            if cy8 > cy6:
                chee = 0
                if "Index" in showfinger:
                    showfinger.remove("Index") 
            else:
                chee = 1 
                if "Index" not in showfinger:
                    showfinger.append("Index")
            if cy12 > cy10:
                klang = 0
                if "Middle" in showfinger:
                    showfinger.remove("Middle")  
            else:
                klang = 1
                if "Middle" not in showfinger:
                    showfinger.append("Middle")
            if cy16 > cy14:
                nang = 0
                if "Ring" in showfinger:
                    showfinger.remove("Ring")  
            else:
                nang = 1
                if "Ring" not in showfinger:
                    showfinger.append("Ring")
            if cy20 > cy18:
                koi = 0
                if "Pinky" in showfinger:
                    showfinger.remove("Pinky")  
            else:
                koi = 1 
                if "Pinky" not in showfinger:
                    showfinger.append("Pinky")   
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, "Finger: " + str(showfinger) , (50, 400), cv2.FONT_HERSHEY_PLAIN, 1,(0, 255, 0), 1)
    cv2.putText(img, "Tanawat Arampraphat" , (450, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)     
    cv2.putText(img, "670610759" , (450, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)               
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()
