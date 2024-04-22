import os

# 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI data'

# 디렉터리 내의 모든 파일을 순회하면서 Excel 파일 찾기
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):  # Excel 파일 확장자 확인
        print(filename)
