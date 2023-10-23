import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 웹캠 초기화
cap = cv2.VideoCapture(0)

# MediaPipe Hands 모델 초기화
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # 손 인식 수행
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # 감지된 손가락 수 세기
        finger_count = 0
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                for point in landmarks.landmark:
                    if point.y < 0.7:
                        finger_count += 1

        # 메시지 작성
        message = str(finger_count)

        # message.txt 파일에 메시지 저장
        with open("message.txt", "w") as file:
            file.write(message)

        # 손가락 및 결과 그리기
        mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Finger Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()