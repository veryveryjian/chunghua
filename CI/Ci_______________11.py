import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 결과를 새 Excel 파일로 저장
output_file = r'C:\Users\charlton\Desktop\CI\filtered_data.xlsx'
df.to_excel(output_file, index=False)

# 선택된 열을 포함하는 새 DataFrame 생성
COUNT = df[['Item', 'Pcs']]

# 결과를 새 Excel 파일로 저장, 시트 이름을 'COUNT'로 설정
output_file_count = r'C:\Users\charlton\Desktop\CI\COUNT.xlsx'
COUNT.to_excel(output_file_count, index=False, sheet_name='COUNT')
