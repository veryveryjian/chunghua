# 아래의 조건을 적용해줘
# 1.  Item열에 데이터 있으면 모든 정보를 가져온다. Item_data 변수로 df 저장
# 2. Item_data df의 인덱스 0-5번 컬럼 중 어느 한 컬럼에 값을 없을 경우 데이터에서 제외, index_null_check이란 변수에 df을 대입
# 3.index_null_check변수의 df의 Item열의 값을 - 기준으로 분리, -기준으로 앞의 텍스트는 Color_code란 열을 만들고 값을 할당, -기준으로 뒤의 텍스트는 Spec_code란 컬럼을 만들고 해당 값을 할당
# 각각의 단계별 df를 출력하는 코드를 추가,
import pandas as pd

# Excel 파일 경로 설정 ('test626.xlsx' 파일 사용)
excel_file = r'C:\Users\charlton\Desktop\test626.xlsx'

# 출력 제한 해제 설정
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# 'INVOICE' 시트에서 B16:G 범위의 데이터 읽어오기
df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

# 'Item' 열에 데이터가 있는 행만 선택하여 'Item_data'에 저장
Item_data = df[df['Item'].notna()]

# 'Item_data'의 첫 6개 컬럼(0-5번) 중 어느 하나라도 값이 없는 행을 제외
index_null_check = Item_data.dropna(subset=Item_data.columns[:6]).copy()  # .copy() 추가하여 명시적으로 복사본 생성

# 'Item' 열의 값을 '-' 기준으로 분리하고, 'Color_code' 열과 'Spec_code' 열 생성 후 값 할당
split_data = index_null_check['Item'].str.split('-', expand=True)
index_null_check.loc[:, 'Color_code'] = split_data[0]  # .loc를 사용하여 값 할당
index_null_check.loc[:, 'Spec_code'] = split_data[1]  # .loc를 사용하여 값 할당

# 결과 출력
print("Item_data DataFrame:")
print(Item_data.head())

print("\nindex_null_check DataFrame:")
print(index_null_check.head())

print("\nDataFrame with Color_code and Spec_code:")
print(index_null_check[['Item', 'Color_code', 'Spec_code']].head())

# 데이터 프레임을 바탕화면에 Excel 파일로 저장
output_file_path = r'C:\Users\charlton\Desktop\Processed_Data.xlsx'
index_null_check.to_excel(output_file_path, index=False, sheet_name='Processed Data')
