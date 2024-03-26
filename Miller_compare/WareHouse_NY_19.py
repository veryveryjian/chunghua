import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Hello_NY.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 'Unnamed: 0' 열을 '-' 기호를 기준으로 분리하고, 결측값을 빈 문자열로 채움
split_data = df['Unnamed: 0'].str.split('-', expand=True).fillna('')

# 분리된 데이터를 새로운 열로 할당
df['Color_Code'] = split_data[0]
df['Model_Code'] = split_data[1]

# 'Unnamed: 0', 'On Hand', 'Code_Part1', 'Code_Part2' 열만 추출
output_df = df[['Unnamed: 0', 'On Hand', 'Color_Code', 'Model_Code']]

# 결과를 엑셀 파일로 저장
output_file_path = 'C:/Users/charlton/Desktop/Ny_ware.xlsx'
output_df.to_excel(output_file_path, index=False)

print("File saved successfully at", output_file_path)

