import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
# skiprows=15는 Excel에서 B16까지의 15행을 건너뛰라는 의미입니다 (1부터 시작하는 행 번호에서 1을 빼서 0부터 시작하는 Python 인덱스로 맞춤).
# usecols='B:G'는 B열부터 G열까지 읽어오라는 의미입니다.
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 읽어온 데이터 출력
print(df)
