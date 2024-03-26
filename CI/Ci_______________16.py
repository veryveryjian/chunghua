import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 'Item'과 'Pcs' 열만 선택하여 새 DataFrame 생성
COUNT = df[['Item', 'Pcs']].copy()

# Pcs 열을 숫자형으로 변환하고, 변환할 수 없는 값은 NaN으로 설정
COUNT['Pcs'] = pd.to_numeric(COUNT['Pcs'], errors='coerce')

# Item 열이 빈 값이 아니고, Pcs가 NaN이 아닌 행만 필터링
filtered_COUNT = COUNT.dropna(subset=['Item', 'Pcs'])

# Item 열의 중복 제거 및 Pcs 열의 합계 계산
# 각 Item별로 Pcs의 합계를 구하고, reset_index()로 DataFrame 형태로 변환
grouped_COUNT = filtered_COUNT.groupby('Item', as_index=False)['Pcs'].sum()

# 'Total' 행 추가 및 Pcs 열의 전체 합계 계산
total_pcs = grouped_COUNT['Pcs'].sum()
total_row = pd.DataFrame([{'Item': 'Total', 'Pcs': total_pcs}])

# grouped_COUNT에 total_row 추가
final_COUNT = pd.concat([grouped_COUNT, total_row], ignore_index=True)

# 결과를 새 Excel 파일로 저장, 시트 이름을 'COUNT'로 설정
output_file_count = r'C:\Users\charlton\Desktop\CI\COUNT_final.xlsx'
final_COUNT.to_excel(output_file_count, index=False, sheet_name='COUNT')

print("최종 COUNT 데이터가 성공적으로 저장되었습니다:", output_file_count)
