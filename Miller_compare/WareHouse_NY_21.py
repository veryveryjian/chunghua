import pandas as pd

# 파일 경로 정의
a_file_path = 'C:/Users/charlton/Desktop/NY_sim.xlsx'
b_file_path = 'C:/Users/charlton/Desktop/MS-room.xlsx'
c_file_path = 'C:/Users/charlton/Desktop/ny_cbm_.xlsx'

# 파일 불러오기d
a_df = pd.read_excel(a_file_path)
b_df = pd.read_excel(b_file_path)
c_df = pd.read_excel(c_file_path)

# a.xlsx 파일 구조 파악
print("a.xlsx File Structure")
print("Columns:", a_df.columns.tolist())  # 컬럼명 출력
print("Data Types:\n", a_df.dtypes)       # 데이터 타입 출력
print("Missing Values:\n", a_df.isnull().sum())  # 결측치 수 출력
print("First 5 Rows:\n", a_df.head())     # 첫 5줄 데이터 출력
print("\n")

# b.xlsx 파일 구조 파악
print("b.xlsx File Structure")
print("Columns:", b_df.columns.tolist())  # 컬럼명 출력
print("Data Types:\n", b_df.dtypes)       # 데이터 타입 출력
print("Missing Values:\n", b_df.isnull().sum())  # 결측치 수 출력
print("First 5 Rows:\n", b_df.head())     # 첫 5줄 데이터 출력
print("\n")

# c.xlsx 파일 구조 파악
print("c.xlsx File Structure")
print("Columns:", c_df.columns.tolist())  # 컬럼명 출력
print("Data Types:\n", c_df.dtypes)       # 데이터 타입 출력
print("Missing Values:\n", c_df.isnull().sum())  # 결측치 수 출력
print("First 5 Rows:\n", c_df.head())     # 첫
