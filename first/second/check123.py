import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Inventory_item/ny.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 데이터프레임의 처음 몇 줄 확인
print("처음 5개 행을 표시합니다:\n", df.head())

# 데이터프레임 정보 확인
print("\n데이터프레임 정보:")
df.info()

# 각 컬럼의 기본 통계 정보 확인
print("\n기본 통계 정보:")
print(df.describe())

# 컬럼 목록 확인
print("\n컬럼 목록:")
print(df.columns.tolist())
