import pandas as pd
from openpyxl import load_workbook

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

# openpyxl을 사용하여 워크북 로드
wb = load_workbook(filename=excel_file)

# 활성 시트의 이름 확인
active_sheet_name = wb.active.title
print(f"활성화된 시트의 이름: {active_sheet_name}")

# pandas를 사용하여 활성화된 시트의 데이터 로드
df = pd.read_excel(excel_file, sheet_name=active_sheet_name)

# 데이터 프레임의 첫 5행 출력
print(df.head())
