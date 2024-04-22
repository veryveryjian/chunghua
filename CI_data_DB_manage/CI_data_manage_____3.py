import pandas as pd

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\test1.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')
print(df)

# 결과를 새 Excel 파일로 저장
output_file = r'C:\Users\charlton\Desktop\filtered_data.xlsx'
df.to_excel(output_file, index=False)

# Excel 파일 전체 로드
# df = pd.read_excel(excel_file, sheet_name='INVOICE')

# 헤더 위치 식별
header_indices = df.index[df['Item'] == 'Item'].tolist()

# 데이터 구간 분리 및 변수 할당
sections = {}  # 각 섹션을 저장할 딕셔너리
for i, start in enumerate(header_indices):
    end = header_indices[i+1] if i+1 < len(header_indices) else None
    section_df = df[start:end].reset_index(drop=True).iloc[1:]  # 헤더 행 제외
    sections[f'section_{i+1}'] = section_df

# 각 섹션 출력
for name, section_df in sections.items():
    print(f"{name}:")
    print(section_df)
    print("\n")

# 예를 들어 첫 번째 섹션을 독립적인 변수로 할당하고 싶다면
section_1 = sections['section_1']
print("Section 1:")

