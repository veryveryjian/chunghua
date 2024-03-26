import pandas as pd

# 파일 경로 정의
ny_test_file_path = 'C:/Users/charlton/Desktop/MS_each.xlsx'
cbm_test_file_path = 'C:/Users/charlton/Desktop/Merged_NY_CBM1234.xlsx'

# 파일 불러오기
MS_each = pd.read_excel(ny_test_file_path)
Merged_NY_CBM1234 = pd.read_excel(cbm_test_file_path)

# 데이터 병합
# 'ITEM'과 'Unnamed: 0'을 기준으로 ny_test_df 데이터에 cbm_test_df의 'On Hand' 데이터를 추가
merged_df = pd.merge(MS_each, Merged_NY_CBM1234[['Unnamed: 0', 'On Hand']], left_on='ITEM', right_on='Unnamed: 0', how='left')

# 'On Hand' 열을 원하는 이름으로 변경 (예: 'OnHandData')
merged_df.rename(columns={'On Hand': 'OnHandData'}, inplace=True)

# 불필요한 'Unnamed: 0' 열 제거
merged_df.drop(columns=['Unnamed: 0','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 0','Unnamed: 10',], inplace=True)

# 결과를 새로운 엑셀 파일로 저장
output_file_path = 'C:/Users/charlton/Desktop/Updated_MS_each.xlsx'
merged_df.to_excel(output_file_path, index=False)

