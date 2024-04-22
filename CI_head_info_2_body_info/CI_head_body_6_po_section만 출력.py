import os
import pandas as pd

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI_Create'

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]

# 각 Excel 파일을 순회하며 처리
for file in excel_files:
    file_path = os.path.join(directory, file)

    # 파일에서 데이터 읽기
    df = pd.read_excel(file_path)

    # 'PO#'로 시작하는 각 주문 섹션의 시작 인덱스 찾기
    po_indices = df.index[df.iloc[:, 0].str.contains("PO#", na=False)].tolist()

    # 파일명 출력
    print(f"\nFile: {file}")

    # 'PO#' 섹션들 출력
    for index in po_indices:
        po_number = df.iloc[index, 0]
        print(f"Found PO Section: {po_number}")
