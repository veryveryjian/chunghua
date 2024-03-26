import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# Excel 파일 읽기, 시트 이름을 'INVOICE'로 수정
df = pd.read_excel(excel_file, sheet_name='INVOICE')

# G7 및 G12 셀의 값을 출력, 위치를 기반으로 접근
# pandas에서 0부터 인덱싱을 시작하므로, Excel의 'G7'은 pandas에서 [6, 6], 'G12'는 [11, 6]
value_g7 = df.iloc[5, 6]  # 7번째 행, 'G'열의 값
value_g12 = df.iloc[10, 6]  # 12번째 행, 'G'열의 값

print(f"G7 셀의 값: {value_g7}")
print(f"G12 셀의 값: {value_g12}")
