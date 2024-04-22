import pandas as pd
import os  # os 모듈을 추가하여 파일 이름을 처리할 수 있도록 함

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# 파일 경로 설정
file_path = r'C:\Users\charlton\Desktop\CI data\PO#127E2  INVOICE（TGBU8731413）.xlsx'

# 데이터프레임으로 엑셀 파일 읽기, 헤더 없음으로 설정
df = pd.read_excel(file_path, sheet_name='INVOICE', header=None)

# 출력할 값의 위치와 설명
positions = [
    (6, 6, "Invoice NO."),
    (9, 1, "Loading date"),
    (7, 6, "Ship date"),
    (9, 6, "Voyage"),
    (10, 6, "B/L NO."),
    (11, 6, "Container No.")
]

# 각 위치에 있는 값을 출력
for row, col, title in positions:
    print(f"{title}: {df.iat[row, col]}")

# 'TOTAL' 문자열이 포함된 행 찾기 (대문자로 검색)
total_row = df[df[0].str.contains('TOTAL', na=False, case=True)].index.tolist()

# 'TOTAL' 문자열이 있는 행의 5번째 열의 값 출력
if total_row:
    for row in total_row:
        total_value = df.iat[row, 5]
        print(f"Row {row} - Total Amount: {total_value}")
else:
    print("No 'TOTAL' string found in the first column.")

# 파일 이름 출력
file_name = os.path.basename(file_path)  # 파일 경로에서 파일 이름만 추출
print(f"Data source file name: {file_name}")
