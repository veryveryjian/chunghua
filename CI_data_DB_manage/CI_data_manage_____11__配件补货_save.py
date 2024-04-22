import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Excel 파일 경로 설정
excel_file = r'C:\Users\charlton\Desktop\test2.xlsx'

# Excel 파일 불러오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=14, usecols='A:G', header=None)


df = df.drop(0).reset_index(drop=True)  # 첫 번째 행 제거 후 인덱스 재설정

# 'PO#'로 시작하는 각 주문 섹션의 시작 인덱스 찾기
po_indices = df.index[df.iloc[:, 0].str.contains("PO#", na=False)].tolist()

# 각 'PO#' 주문 섹션을 별도의 데이터프레임으로 추출
po_sections = {}
for i, start_index in enumerate(po_indices):
    # 다음 PO# 섹션 시작점 또는 데이터 프레임의 끝까지를 섹션으로 설정
    end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
    section_df = df.iloc[start_index:end_index].reset_index(drop=True)

    # 마지막 섹션에만 무효한 데이터 행 제거 적용
    if i == len(po_indices) - 1:  # 마지막 섹션 확인
        section_df = section_df.dropna(subset=df.columns[1:7], how='all')

    po_sections[f'po_section_{i}'] = section_df

# 각 PO# 주문 섹션 데이터프레임 출력
for name, section in po_sections.items():
    print(f"{name}:")
    print(section)
    print("\n")
