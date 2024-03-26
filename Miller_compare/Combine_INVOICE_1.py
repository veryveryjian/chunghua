import pandas as pd
from pathlib import Path

# 파일 경로 설정
desktop_path = Path("C:/Users/charlton/Desktop/test")
file_names = ["S27730.csv", "S27741.csv"]  # 이 부분을 동적으로 구성

# 여러 파일을 불러와 하나의 데이터프레임으로 결합
df_list = []
for file_name in file_names:
    file_path = desktop_path / file_name
    df_temp = pd.read_csv(file_path, encoding='ISO-8859-1')
    df_list.append(df_temp)

df_combined = pd.concat(df_list, ignore_index=True)

# 'Debit'와 'Credit'을 사용해 'Amount' 계산 및 필요한 열 선택
df_combined['Amount'] = df_combined['Debit'] - df_combined['Credit']
df_selected = df_combined[['Item', 'Qty', 'Credit', 'Amount']]

# 피벗 테이블 생성
pivot_table = df_selected.groupby('Item').agg({'Qty': 'sum', 'Credit': 'sum', 'Amount': 'sum'}).reset_index()

# 출력 파일 이름 동적 생성
output_filename = f"{file_names[0].split('.')[0]}_combined.xlsx"
output_path = desktop_path / output_filename

# 엑셀 파일로 저장
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_selected.to_excel(writer, sheet_name='Raw_Data', index=False)
    pivot_table.to_excel(writer, sheet_name='Summary', index=False)

    # 추가적인 분석 결과를 여기에 저장할 수 있습니다.
