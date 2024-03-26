import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Hello_NY.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 'Unnamed: 0' 및 'Sales/Week' 열 출력
print(df[['Unnamed: 0', 'On Hand']])
