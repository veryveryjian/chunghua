import pandas as pd

# 파일 경로 정의
ny_test_file_path = 'C:/Users/charlton/Desktop/po_ms.xlsx'
cbm_test_file_path = 'C:/Users/charlton/Desktop/CBM_test.xlsx'

# 파일 불러오기
ny_test_df = pd.read_excel(ny_test_file_path)
cbm_test_df = pd.read_excel(cbm_test_file_path)

# JIN# 번호 입력
jin_number = 348  # 여기에 원하는 번호를 입력하세요.

# 'JIN#XXX-MS' 열 이름 생성
column_name = f'JIN#{jin_number}-MS'

# CODE 열을 기준으로 두 데이터프레임 결합
# 여기서 'Code'와 'CODE'가 올바른 열 이름인지 확인하세요.
merged_df = ny_test_df.merge(cbm_test_df, left_on='Code', right_on='CODE', how='left')

# 필요한 열이 있는지 확인
if column_name in merged_df.columns:
    # 입력된 JIN# 열의 값과 CBM 값을 곱함
    merged_df['Total_CBM'] = merged_df[column_name] * merged_df['CBM']

    # 총합 계산 및 출력
    total_sum = merged_df['Total_CBM'].sum()
    print(f'Total CBM for JIN#{jin_number}: {total_sum}')

    # 결과 데이터프레임 준비
    result_df = merged_df[['Item', column_name, 'CBM', 'Total_CBM']]

    # 엑셀 파일로 저장
    output_file_path = f'C:/Users/charlton/Desktop/Calculation_Result_JIN#{jin_number}.xlsx'
    result_df.to_excel(output_file_path, index=False)
    print(f'Results saved to {output_file_path}')
else:
    print(f'Column {column_name} not found in the dataframe.')

