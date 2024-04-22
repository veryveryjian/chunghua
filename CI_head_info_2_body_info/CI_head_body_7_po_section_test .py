import os
import pandas as pd

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI_data_r2'

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]

# 각 Excel 파일을 순회하며 처리
for file in excel_files:
    file_path = os.path.join(directory, file)
    print(f"\nProcessing File: {file}")

    # 파일에서 데이터 읽기
    df = pd.read_excel(file_path)

    # 'PO#'로 시작하는 각 섹션의 시작 인덱스와 'TOTAL'로 끝나는 섹션의 종료 인덱스 찾기
    po_indices = df.index[df.iloc[:, 0].str.contains("^PO#", na=False)].tolist()
    total_indices = df.index[df.iloc[:, 0].str.contains("TOTAL", na=False, case=True)].tolist() + \
                    df.index[df.iloc[:, 0].str.contains("Total", na=False, case=True)].tolist()

    # 각 'PO#' 섹션 정보 추출
    for start_index in po_indices:
        # 해당 'PO#' 섹션의 종료 인덱스 찾기
        end_index = next((i for i in total_indices if i > start_index), None)

        if end_index:
            # 'PO#' 값 추출
            po_number = df.iloc[start_index, 0]
            # 'TOTAL' 값 추출
            total_value = df.iloc[end_index, 5]

            print(f"Section: {po_number}")
            print(f"Starts at index: {start_index}, Ends at index: {end_index}")
            print(f"Total Value: {total_value}")
        else:
            print(f"Section: {po_number} has no clear end with 'TOTAL'")
