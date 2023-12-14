import dlib
import cv2
from glob import glob
from tqdm import tqdm
import os

# 얼굴 랜드마크 모델 경로
predictor_path = r"shape_predictor_68_face_landmarks.dat"

# 얼굴 디텍터 생성
detector = dlib.get_frontal_face_detector()

# 얼굴 랜드마크 예측기 생성
predictor = dlib.shape_predictor(predictor_path)

# 이미지 파일 경로
image_paths = glob(r"train\images\*.jpg")

for image_path in tqdm(image_paths, total=len(image_paths)):
    # 이미지 불러오기
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 영역 검출
    faces = detector(gray)

    # 각 얼굴에 대한 랜드마크 확인
    height, width = gray.shape

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = ['1']
        right_eye = ['1']

        for n in range(36, 42):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            left_eye.append(str(x / width))
            left_eye.append(str(y / height))

        for n in range(42, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            right_eye.append(str(x / width))
            right_eye.append(str(y / height))

        # 텍스트 파일 경로
        file_path = r"train\labels"+"\\"+os.path.basename(image_path)[:-3]+"txt"

        # 파일 열기 (읽기 모드로)
        with open(file_path, "r") as file:
            # 파일의 내용을 읽어옴
            file_content = file.read()

        with open(file_path, "a") as file:
            # 파일 내용 출력
            if '1' not in [segment.split(' ')[0] for segment in file_content.split('\n')]:
                file.write(' '.join(left_eye) if len(file_content) == 0 else "\n"+' '.join(left_eye))
                file.write("\n"+' '.join(right_eye))