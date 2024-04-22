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

# 'Item' 열의 값을 '-' 기준으로 첫 번째 대시에서만 분리하고, 'Color_code' 열과 'spec_code' 열 생성 후 값 할당
split_data = index_null_check['Item'].str.split('-', n=1, expand=True)  # 첫 번째 '-'에서만 분리하도록 변경
index_null_check['Color_code'] = split_data[0]
index_null_check['spec_code'] = split_data[1]  # 'spec_code'에는 'GLASS DOOR' 포함 뒷부분이 저장됩니다.

# 나머지 코드는 이전과 동일

# CBM 엑셀 파일 경로 설정 ('CBM.xlsx' 파일 사용)
cbm_file_path = r'C:\Users\charlton\Desktop\CBM.xlsx'

# CBM 엑셀 파일 읽어오기
CBM_df = pd.read_excel(cbm_file_path)

# spec_code를 기준으로 index_null_check 데이터와 CBM 데이터를 left join
merged_df = pd.merge(index_null_check, CBM_df, on='spec_code', how='left')

# 'cbmXqty' 열 추가: 'CBM' 열과 'Pcs' 열의 값을 곱하여 새 열에 할당
merged_df['cbmXqty'] = merged_df['CBM'] * merged_df['Pcs']

# 병합된 데이터 프레임을 바탕화면에 Excel 파일로 저장 (첫번째 시트)
output_merged_file_path = r'C:\Users\charlton\Desktop\Joined_Data.xlsx'
with pd.ExcelWriter(output_merged_file_path, engine='xlsxwriter') as writer:
    merged_df.to_excel(writer, index=False, sheet_name='Joined Data')

    # Color_code로 그룹화하고 cbmXqty의 합계를 계산하여 새로운 시트에 저장
    summary_df = merged_df.groupby('Color_code')['cbmXqty'].sum().reset_index()
    summary_df.to_excel(writer, index=False, sheet_name='Summary by Color')

# 병합된 데이터프레임 출력
print("Merged DataFrame:")
print(merged_df.head())
