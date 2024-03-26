import pandas as pd

# 파일 경로를 리스트로 저장
file_paths = [
    'C:/Users/charlton/Desktop/Inventory_item/ct.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/mi.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/nj.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/ny.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/pa.CSV'
]

# CSV 파일 불러와서 상위 5개 행 출력
for path in file_paths:
    try:
        df = pd.read_csv(path)
    except UnicodeDecodeError:
        # 유니코드 디코드 에러 발생 시 다른 인코딩으로 시도
        df = pd.read_csv(path, encoding='latin1')
    print(f"파일: {path}")
    print(df.head())
    print("\n")

# Excel 파일은 별도로 처리
excel_path = 'C:/Users/charlton/Desktop/MS_each.xlsx'
df = pd.read_excel(excel_path)
print(f"파일: {excel_path}")
print(df.head())
