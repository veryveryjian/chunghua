#CI_Create에 생성된 데이터를 기반으로 함!
#각 팔일을 섹션을 짤라서 [출력]으로만 보는 것
import os
import pandas as pd

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI_Create'

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]

# 각 Excel 파일을 순회하며 처리
for file in excel_files:
    file_path = os.path.join(directory, file)
    print(f"Processing File: {file}")

    # 파일에서 데이터 읽기
    df = pd.read_excel(file_path)

    # 'PO#'로 시작하는 각 주문 섹션의 시작 인덱스 찾기
    po_indices = df.index[df.iloc[:, 0].str.contains("PO#", na=False)].tolist()

    # 각 'PO#' 주문 섹션을 별도의 데이터프레임으로 추출
    po_sections = {}
    for i, start_index in enumerate(po_indices):
        end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
        section_df = df.iloc[start_index:end_index].reset_index(drop=True)
        po_sections[f'po_section_{i}'] = section_df

    # 각 PO# 주문 섹션 데이터프레임 출력
    for name, section in po_sections.items():
        print(f"{name}:")
        print(section)
        print("\n")
