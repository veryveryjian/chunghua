import os
import pandas as pd

# 출력 제한 해제
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\test2'

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]
# print(f"Found {len(excel_files)} Excel files in the directory.")

# 각 Excel 파일을 순회하며 처리
for file in excel_files:
    file_path = os.path.join(directory, file)
    # print(f"\nProcessing File: {file} located at {file_path}")

    # 파일에서 데이터 읽기
    df = pd.read_excel(file_path)
    # print(f"Loaded data from {file}, shape: {df.shape}")

    # 'TOTAL' 문자열이 일부분으로 포함된 행 찾기
    total_rows = df[df.iloc[:, 0].str.contains("TOTAL", na=False, case=True)]
    # print(f"Found {len(total_rows)} rows containing 'TOTAL' in {file}")

    if total_rows.empty:
        print(f"No rows containing 'TOTAL' found in {file}.")
    else:
        # 각 'TOTAL' 행의 5번 컬럼 값 출력
        for index, total_row in total_rows.iterrows():
            total_value = total_row.iloc[5]  # 위치 기반 인덱싱으로 변경
            print(f"Row {index} - {file} - Total Value: {total_value}")
