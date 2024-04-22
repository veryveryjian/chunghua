import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

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

# 새 Excel 워크북 생성
wb = Workbook()
wb.remove(wb.active)  # 기본 시트 삭제

# 각 'PO#' 주문 섹션을 별도의 데이터프레임으로 추출 및 각 섹션을 별도의 시트로 저장
final = {}
for i, start_index in enumerate(po_indices):
    end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
    section_df = df.iloc[start_index:end_index].reset_index(drop=True)

    # 마지막 섹션에만 무효한 데이터 행 제거 적용
    if i == len(po_indices) - 1:  # 마지막 섹션 확인
        section_df = section_df.dropna(subset=df.columns[1:7], how='all')

    # 시트 이름 설정 (첫 행, 첫 열 값)
    sheet_name = str(section_df.iloc[0, 0])

    # 시트 생성 및 데이터 쓰기
    ws = wb.create_sheet(title=sheet_name)
    for r in dataframe_to_rows(section_df, index=False, header=True):
        ws.append(r)

    final[f'po_section_{i}'] = section_df


# 파일 저장
output_file_path = excel_file.replace('.xlsx', '_r.xlsx')
wb.save(filename=output_file_path)



print("Excel 파일이 저장되었습니다:", output_file_path)
