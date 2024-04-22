import os
import openpyxl

# 해당 경로 지정
directory = r'C:\Users\charlton\Desktop\download'

# 경로에서 모든 파일 목록을 가져와서 엑셀 파일(.xlsx)만 필터링
excel_files = [file for file in os.listdir(directory) if file.endswith('.xlsx')]

# 엑셀 파일이 있는지 확인
if excel_files:
    for excel_file in excel_files:
        # 파일 경로 완성
        file_path = os.path.join(directory, excel_file)

        # 엑셀 파일 로드
        workbook = openpyxl.load_workbook(file_path)

        # 모든 시트의 이름을 출력
        sheet_names = workbook.sheetnames
        print(f"파일명: {excel_file}, 시트 이름: {sheet_names}")
else:
    print("해당 폴더에 엑셀 파일이 없습니다.")
