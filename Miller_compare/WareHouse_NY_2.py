import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Hello_NY.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 'Unnamed: 0' 열을 '-' 기호를 기준으로 분리하고, 결측값을 빈 문자열로 채움
split_data = df['Unnamed: 0'].str.split('-', expand=True).fillna('')

# 분리된 데이터를 새로운 열로 할당
df['Color_Code'] = split_data[0]
df['Model_Code'] = split_data[1]  # 오타 수정: Molel_Code -> Model_Code

# 'Unnamed: 0', 'On Hand', 'Color_Code', 'Model_Code' 열만 추출하여 data_1에 할당
data_1 = df[['Unnamed: 0', 'On Hand', 'Color_Code', 'Model_Code']]

# 결과를 엑셀 파일에 저장
output_file_path = 'C:/Users/charlton/Desktop/Ny_test.xlsx'

# 'Color_Code' 열에서 특정 값에 해당하는 행만 필터링하여 새로운 데이터프레임 생성
filtered_data = data_1[data_1['Color_Code'].isin(['CW2', 'E2', 'MS', 'SE', 'SG'])]

# pandas의 ExcelWriter를 사용하여 엑셀 파일에 새로운 시트로 저장
with pd.ExcelWriter(output_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    filtered_data.to_excel(writer, sheet_name='data_1', index=False)

print("Filtered data saved successfully in 'data_1' sheet at", output_file_path)
