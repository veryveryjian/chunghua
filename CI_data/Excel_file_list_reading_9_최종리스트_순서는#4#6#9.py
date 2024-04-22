#CI_Create의 파일을 동일 경로에 한개의 엑셀 파일을 생성
#section file / section number를 생성함 : 예상치 못한 건데 좋음.
#데이터 전처리 : 어떻게 하면 데이터베이스 형태로 만들 수 있을까?
#문제점 : buhuo 그건 어떻게 선별하지 ㅎㅎㅎㅎ
#엑셀시트로 각각 섹션 유의미함, 두개를 비교하면 답을 찾을 수 있음.
#문제점 : total 이런거 없어야 됨.
#생각해 보자.

import os
import pandas as pd

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI_Create'
output_directory = r'C:\Users\charlton\Desktop\CI_total'

# 출력 디렉터리 생성 (존재하지 않는 경우)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 결과를 저장할 데이터프레임 초기화
all_sections_df = pd.DataFrame()

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

    # 각 'PO#' 주문 섹션을 별도의 데이터프레임으로 추출하고 모든 데이터를 하나의 데이터프레임에 추가
    for i, start_index in enumerate(po_indices):
        end_index = po_indices[i + 1] if i + 1 < len(po_indices) else len(df)
        section_df = df.iloc[start_index:end_index].reset_index(drop=True)

        # 파일명과 섹션 번호를 컬럼으로 추가
        section_df['SourceFile'] = file
        section_df['SectionNumber'] = df.iloc[start_index, 0]  # 'PO#' 값을 사용

        # 결과 데이터프레임에 추가
        all_sections_df = pd.concat([all_sections_df, section_df], ignore_index=True)

# 결과 데이터 저장
output_path = os.path.join(output_directory, 'All_PO_Sections.xlsx')
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    all_sections_df.to_excel(writer, sheet_name='All_PO_Sections', index=False)

print(f"All data has been saved to {output_path}")
