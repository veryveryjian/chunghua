import pandas as pd

# 출력 제한 해제 설정
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# Excel 파일 경로 설정 ('test626.xlsx' 파일 사용)
excel_file = r'C:\Users\charlton\Desktop\test626.xlsx'

# 'INVOICE' 시트에서 B16:G 범위의 데이터 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 'Item' 열에 데이터가 있는 행만 선택하여 'Item_data'에 저장
Item_data = df[df['Item'].notna()]

# 'Item_data'의 첫 6개 컬럼(0-5번) 중 어느 하나라도 값이 없는 행을 제외
index_null_check = Item_data.dropna(subset=Item_data.columns[:6]).copy()

# 'Item' 열의 값을 '-' 기준으로 분리하고, 'Color_code' 열과 'Spec_code' 열 생성 후 값 할당
split_data = index_null_check['Item'].str.split('-', expand=True)
index_null_check['Color_code'] = split_data[0]
index_null_check['spec_code'] = split_data[1]

# CBM 엑셀 파일 경로 설정 ('CBM.xlsx' 파일 사용)
cbm_file_path = r'C:\Users\charlton\Desktop\CBM.xlsx'

# CBM 엑셀 파일 읽어오기
CBM_df = pd.read_excel(cbm_file_path)

# spec_code를 기준으로 index_null_check 데이터와 CBM 데이터를 left join
merged_df = pd.merge(index_null_check, CBM_df, on='spec_code', how='left')

# 병합된 데이터 프레임을 바탕화면에 Excel 파일로 저장
output_merged_file_path = r'C:\Users\charlton\Desktop\Joined_Data.xlsx'
merged_df.to_excel(output_merged_file_path, index=False, sheet_name='Joined Data')

# 병합된 데이터프레임 출력
print("Merged DataFrame:")
print(merged_df.head())
