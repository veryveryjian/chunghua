import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# Excel 파일 읽기, 시트 이름을 'INVOICE'로 수정
df = pd.read_excel(excel_file, sheet_name='INVOICE')

# 엑셀을 기준으로 한다: Excel은 1부터 시작하지만, pandas는 0부터 시작한다.
# 따라서 Excel의 'G7' 셀은 pandas에서 [5, 6]에 해당하고, 'G12' 셀은 [10, 6]에 해당한다.
value_g7 = df.iloc[5, 6]  # 6번째 행, 'G'열의 값 (Excel의 'G7'에 해당)
value_g12 = df.iloc[10, 6]  # 11번째 행, 'G'열의 값 (Excel의 'G12'에 해당)

print(f"G7 셀의 값: {value_g7}")
print(f"G12 셀의 값: {value_g12}")
