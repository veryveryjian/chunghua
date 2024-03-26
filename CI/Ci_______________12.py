import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 결과를 새 Excel 파일로 저장
output_file = r'C:\Users\charlton\Desktop\CI\filtered_data.xlsx'
df.to_excel(output_file, index=False)

# 'Item'과 'Pcs' 열만 선택하여 새 DataFrame 생성
COUNT = df[['Item', 'Pcs']].copy()

# Pcs 열을 숫자형으로 변환하고, 변환할 수 없는 값은 NaN으로 설정
COUNT['Pcs'] = pd.to_numeric(COUNT['Pcs'], errors='coerce')

# Item 열이 빈 값이 아니고, Pcs가 NaN이 아닌 행만 필터링
filtered_COUNT = COUNT.dropna(subset=['Item', 'Pcs'])

# 결과를 새 Excel 파일로 저장, 시트 이름을 'COUNT'로 설정
output_file_count = r'C:\Users\charlton\Desktop\CI\COUNT_filtered.xlsx'
filtered_COUNT.to_excel(output_file_count, index=False, sheet_name='COUNT')

print("필터링된 COUNT 데이터가 성공적으로 저장되었습니다:", output_file_count)
