import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

excel_file = r'C:\Users\charlton\Desktop\test1.xlsx'
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='A:G')
print(df)


# PO# 주문 섹션의 시작 인덱스를 찾기
po_indices = df.index[df.iloc[:, 0].str.contains("PO#", na=False)].tolist()
print(po_indices)

# 각 PO# 주문 섹션을 별도의 데이터프레임으로 추출하여 변수에 할당
po_sections = {}
for i, start_index in enumerate(po_indices):
    end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
    # 첫 번째 행(헤더)을 포함하고, 그 다음 행부터 데이터를 추출하도록 조정
    po_sections[f'po_section_{i + 1}'] = df.iloc[start_index:end_index].reset_index(drop=True)

# 각 PO# 주문 섹션 데이터프레임 출력 및 변수에 할당 예시
for name, section in po_sections.items():
    print(f"{name}:")
    # 첫 번째 NaN 행을 제외하고 출력
    print(section.iloc[1:])
    print("\n")


