import pandas as pd

# 파일 경로 정의
ny_test_file_path = 'C:/Users/charlton/Desktop/po_ms.xlsx'
cbm_test_file_path = 'C:/Users/charlton/Desktop/CBM_test.xlsx'
price_file_path = 'C:/Users/charlton/Desktop/price.xlsx'

# 파일 불러오기
ny_test_df = pd.read_excel(ny_test_file_path)
cbm_test_df = pd.read_excel(cbm_test_file_path)
price_df = pd.read_excel(price_file_path)

# JIN# 번호 입력
jin_number = 354  # 원하는 번호로 변경 가능

# 'JIN#XXX-MS' 열 이름 생성
column_name = f'JIN#{jin_number}-MS'

# CODE 열을 기준으로 두 데이터프레임 결합
merged_df = ny_test_df.merge(cbm_test_df, left_on='Code', right_on='CODE', how='left')

# Price 데이터프레임 결합
final_df = merged_df.merge(price_df, on='Code', how='left')

# Total_Price 계산
final_df['Total_Price'] = final_df[column_name] * final_df['Price']

# 필요한 열이 있는지 확인
if column_name in final_df.columns:
    # Total_Price의 총합 계산 및 출력
    total_price = final_df['Total_Price'].sum()
    print(f'Total Price for JIN#{jin_number}: {total_price}')

    # 결과 데이터프레임 준비
    # 여기서는 'Total_CBM' 대신 'CBM'을 사용해야 합니다.
    result_df = final_df[['Item', 'Code', column_name, 'CBM', 'Price', 'Total_Price']].copy()

    # 엑셀 파일로 저장
    output_file_path = f'C:/Users/charlton/Desktop/Calculation_Result_JIN#{jin_number}_price.xlsx'
    result_df.to_excel(output_file_path, index=False)
    print(f'Results saved to {output_file_path}')
else:
    print(f'Column {column_name} not found in the dataframe.')



