import pandas as pd
from pathlib import Path

# 파일 경로 설정
desktop_path = Path("C:/Users/charlton/Desktop/test")
ir_file_names = ["IR4847.csv",
                 "IR4849.csv",]  # 이 부분을 동적으로 구성할 수 있음

# 여러 파일을 불러와 하나의 데이터프레임으로 결합
df_ir_list = []
for file_name in ir_file_names:
    file_path = desktop_path / file_name
    df_temp = pd.read_csv(file_path, encoding='ISO-8859-1')
    df_ir_list.append(df_temp)

df_ir_combined = pd.concat(df_ir_list, ignore_index=True)

# 필요한 열 선택 및 데이터 처리
df_ir_selected = df_ir_combined[['Item', 'Qty', 'Amount']]

# 피벗 테이블 생성
ir_pivot_table = df_ir_selected.groupby('Item').agg({'Qty': 'sum', 'Amount': 'sum'}).reset_index()

# 출력 파일 이름 동적 생성
output_ir_filename = f"IR_combined.xlsx"
output_ir_path = desktop_path / output_ir_filename

# 엑셀 파일로 저장
with pd.ExcelWriter(output_ir_path, engine='openpyxl') as writer:
    df_ir_selected.to_excel(writer, sheet_name='IR_Raw_Data', index=False)
    ir_pivot_table.to_excel(writer, sheet_name='IR_Summary', index=False)

    # 여기에 추가적인 분석 결과를 저장할 수 있습니다.
