import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Inventory_item/ny.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 'Unnamed: 0' 열을 첫 번째 '-' 기호를 기준으로 분리
# 'expand=True'는 키워드 인수로 제공
split_data = df['Unnamed: 0'].str.split('-', n=1, expand=True)

# 분리된 데이터를 새로운 열로 할당
df['Color_Code'] = split_data[0]
df['Model_Code'] = split_data[1]  # 오타 수정: Molel_Code -> Model_Code

# 'Unnamed: 0', 'On Hand', 'Color_Code', 'Model_Code' 열만 추출하여 저장
output_df = df[['Unnamed: 0', 'On Hand', 'Color_Code', 'Model_Code']]

# 결과를 엑셀 파일로 저장
output_file_path = 'C:/Users/charlton/Desktop/aaa1.xlsx'
output_df.to_excel(output_file_path, index=False)

print("파일이 성공적으로 저장되었습니다:", output_file_path)
