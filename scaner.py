import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # одна рука
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def finger_status(hand_landmarks):

    fingers = []

    fingers.append(hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x)

    fingers.append(hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y)   # указательный
    fingers.append(hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y) # средний
    fingers.append(hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y) # безымянный
    fingers.append(hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y) # мизинец

    return fingers

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            #fingers = finger_status(handLms)

            # # Жесты:
            # if fingers == [False, True, False, False, False]:
            #     cv2.putText(img, "NEXT", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
            #     pyautogui.press("right")  # перемотка вперед
            #
            # elif fingers == [False, True, True, False, False]:
            #     cv2.putText(img, "VOLUME UP", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 3)
            #     pyautogui.press("volumeup")
            #
            # elif fingers == [False, False, False, False, False]:
            #     cv2.putText(img, "VOLUME DOWN", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)
            #     pyautogui.press("volumedown")
            #
            # elif fingers == [True, True, True, True, True]:
            #     cv2.putText(img, "PLAY/PAUSE", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 3)
            #     pyautogui.press("space")

    cv2.imshow("WebCam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
