import pandas as pd

# 설정 (사용자가 실제로 실행할 수 없는 환경이므로 경로는 예시로 남깁니다.)
excel_file = r'C:\Users\charlton\Desktop\test1.xlsx'  # 예시 경로
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=14, usecols='A:G', header=None)

# 첫 번째 행을 헤더로 설정 및 데이터 전처리
df = df.drop(0).reset_index(drop=True)

# 4번째 - pcs 열을 기준으로 NaN이 아닌 행만 선택
df_item_remove = df.dropna(subset=[4])

# PO# 주문 섹션의 시작 인덱스 찾기
po_indices = df_item_remove.index[df_item_remove.iloc[:, 0].str.contains("PO#", na=False)].tolist()

# 각 PO# 주문 섹션을 별도의 데이터프레임으로 추출
po_sections_remove = {}
for i, start_index in enumerate(po_indices):
    end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df_item_remove)
    section_df = df_item_remove.iloc[start_index:end_index].reset_index(drop=True)
    po_name = section_df.iloc[0, 0]  # PO# 이름 추출
    po_sections_remove[po_name] = section_df

# 각 섹션을 별도의 엑셀 파일로 저장
for po_name, section_df in po_sections_remove.items():
    file_path = f"C:\\Users\\charlton\\Desktop\\{po_name}.xlsx"  # 파일 경로 및 이름 설정
    section_df.to_excel(file_path, index=False)  # 엑셀 파일로 저장

# 코드 실행 결과 확인을 위한 출력 대신 저장 경로 예시 출력
example_file_paths = [f"C:\\Users\\charlton\\Desktop\\{name}.xlsx" for name in po_sections_remove.keys()]
example_file_paths
