import pandas as pd

# 파일의 절대 경로
ms_each_path = 'C:/Users/charlton/Desktop/MS_each.xlsx'  # 실제 파일 경로로 변경하세요
merged_ny_cbm1234_path = 'C:/Users/charlton/Desktop/Merged_NY_CBM1234.xlsx'  # 실제 파일 경로로 변경하세요

# 엑셀 파일 로드
ms_each_df = pd.read_excel(ms_each_path)
merged_ny_cbm1234_df = pd.read_excel(merged_ny_cbm1234_path)

# 'Unnamed: 0' 열을 기준으로 데이터 병합, 필요한 열만 선택
result_df = pd.merge(ms_each_df, merged_ny_cbm1234_df[['Unnamed: 0', 'On Hand']], left_on='Unnamed: 0', right_on='Unnamed: 0', how='left')

# 'On Hand' 열 이름을 'OnHandData'로 변경
result_df.rename(columns={'On Hand': 'OnHandData'}, inplace=True)

# 결과를 새 엑셀 파일로 저장
result_df.to_excel('C:/Users/charlton/Desktop/Updated_MS_each.xlsx', index=False)
