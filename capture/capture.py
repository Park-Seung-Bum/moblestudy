import cv2
import os
import pymysql

# MySQL 연결 설정
db = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mobledb'
)

# 이미지 저장 디렉토리 설정
image_dir = 'capture/image'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# 웹캠 열기
cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)

# 이미지 카운터 초기화
image_counter = 1

while True:
    ret, frame = cap.read()

    # 웹캠 프레임 표시
    cv2.imshow('Webcam', frame)

    # 스페이스바를 누르면 캡처
    key = cv2.waitKey(1)
    if key == ord(' '):
        # 이미지를 파일로 저장
        image_name = os.path.join(image_dir, f'capture_{image_counter}.png')
        cv2.imwrite(image_name, frame)
        print(f'캡처된 이미지를 {image_name}에 저장했습니다.')

        # 이미지 파일 경로를 데이터베이스에 저장
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO photo_data (photo_path) VALUES (%s)",
                           (image_name,))
            db.commit()
            cursor.close()
            print(f'캡처된 이미지 파일 경로를 데이터베이스에 저장했습니다.')
        except Exception as e:
            print(f'데이터베이스에 저장 중 오류 발생: {str(e)}')

        image_counter += 1

    # 'q'를 누르면 종료
    if key == ord('q'):
        break

# 웹캠 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()

# MySQL 연결 닫기
db.close()