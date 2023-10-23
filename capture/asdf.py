import cv2

# 웹캠 열기
cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("웹캠에서 프레임을 읽을 수 없습니다.")
        break

    # 이미지 프레임 크기 확인
    if frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()