import pandas as pd

# 파일 경로 정의
ny_test_file_path = 'C:/Users/charlton/Desktop/Ny_sim2.xlsx'
cbm_test_file_path = 'C:/Users/charlton/Desktop/CBM_test.xlsx'

# Ny_test.xlsx 파일 불러오기
ny_test_df = pd.read_excel(ny_test_file_path)
# CBM_test.xlsx 파일 불러오기
cbm_test_df = pd.read_excel(cbm_test_file_path)

# Ny_test.xlsx 파일 구조 파악
print("Ny_sim2.xlsx File Structure")
print("Columns:", ny_test_df.columns.tolist())  # 컬럼명 출력
print("Data Types:\n", ny_test_df.dtypes)       # 데이터 타입 출력
print("Missing Values:\n", ny_test_df.isnull().sum())  # 결측치 수 출력
print("First 5 Rows:\n", ny_test_df.head())     # 첫 5줄 데이터 출력
print("\n")

# CBM_test.xlsx 파일 구조 파악
print("CBM_test.xlsx File Structure")
print("Columns:", cbm_test_df.columns.tolist())  # 컬럼명 출력
print("Data Types:\n", cbm_test_df.dtypes)       # 데이터 타입 출력
print("Missing Values:\n", cbm_test_df.isnull().sum())  # 결측치 수 출력
print("First 5 Rows:\n", cbm_test_df.head())     # 첫 5줄 데이터 출력
