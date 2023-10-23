from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import cv2
import base64

def capture_image(request):
    cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)

        if key == ord(' '):
            # 이미지를 파일로 저장
            image_name = f'capture_{Image.objects.count() + 1}.png'
            cv2.imwrite(image_name, frame)

            # 이미지를 바이너리 데이터로 변환
            _, buffer = cv2.imencode('.png', frame)
            image_data = buffer.tobytes()

            # 데이터베이스에 저장
            Image.objects.create(image_name=image_name, image_data=image_data)
            break

    cap.release()
    cv2.destroyAllWindows()
    return HttpResponse('이미지 캡처 및 저장 완료')