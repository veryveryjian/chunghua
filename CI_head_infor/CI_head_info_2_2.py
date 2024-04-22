import pandas as pd

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# 파일 경로 설정
file_path = r'C:\Users\charlton\Desktop\CI data\PO#127E2  INVOICE（TGBU8731413）.xlsx'

# 데이터프레임으로 엑셀 파일 읽기
df = pd.read_excel(file_path, sheet_name='INVOICE', header=None)

print(df)

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
