import os
import pandas as pd

# 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI data'

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]

# 실패한 파일 목록 초기화
failed_files = []

# 각 Excel 파일에 대해 포함된 시트 이름 출력
for file in excel_files:
    file_path = os.path.join(directory, file)
    try:
        # 파일 열기
        xls = pd.ExcelFile(file_path)
        print(f"File: {file}")
        for sheet_name in xls.sheet_names:
            print(f"  Sheet: {sheet_name}")
        print("\n")  # 파일 간 구분을 위해 빈 줄 추가
    except Exception as e:
        print(f"Failed to read {file}: {e}")
        failed_files.append(file)

# 실패한 파일 목록 출력
if failed_files:
    print("Failed to read the following files:")
    for failed_file in failed_files:
        print(failed_file)
