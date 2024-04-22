import pandas as pd

# Excel 파일 경로 및 시트 지정
excel_file = r'C:\Users\charlton\Desktop\test1.xlsx'

# 데이터 로드 (헤더 없이 모든 데이터를 로드)
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=14, header=None, usecols='A:G')

# "PO#"로 시작하는 행만 찾아 해당 컬럼의 값을 출력
for index, row in df.iterrows():
    if str(row[0]).startswith("PO#"):
        print(row[0])
