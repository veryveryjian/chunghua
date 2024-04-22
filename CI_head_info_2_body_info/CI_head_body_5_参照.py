import os
import pandas as pd

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI_Create'
output_directory = r'C:\Users\charlton\Desktop\CI_Create\Processed'

# 출력 디렉터리 생성 (존재하지 않는 경우)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

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

    # Excel writer 초기화
    output_path = os.path.join(output_directory, f"{os.path.splitext(file)[0]}_sections.xlsx")
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # 각 'PO#' 주문 섹션을 별도의 데이터프레임으로 추출하고 저장
        for i, start_index in enumerate(po_indices):
            end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
            section_df = df.iloc[start_index:end_index].reset_index(drop=True)

            # 시트 이름 설정 (PO# 이름 사용)
            # 'PO#'가 있는 셀의 값을 시트 이름으로 설정
            sheet_name = str(df.iloc[start_index, 0])
            section_df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Data from {file} saved to {output_path}")
