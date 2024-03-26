import pandas as pd

# Ny_test.xlsx 파일에서 데이터 불러오기
ny_test_df = pd.read_excel('C:/Users/charlton/Desktop/aaa.xlsx')

# CBM_test.xlsx 파일에서 데이터 불러오기
cbm_test = pd.read_excel('C:/Users/charlton/Desktop/CBM_test.xlsx')

# ny_test_df와 cbm_test를 Molel_Code와 CODE 열을 기준으로 결합
merged_df = pd.merge(ny_test_df, cbm_test, how='left', left_on='Model_Code', right_on='CODE')

# 결과를 새로운 엑셀 파일로 저장
merged_file_path = 'C:/Users/charlton/Desktop/Merged_NY_CBM1234.xlsx'
merged_df.to_excel(merged_file_path, index=False)

print("Merged data saved successfully at", merged_file_path)


