import pandas as pd

# 기존 MS_each 엑셀 파일 불러오기
ms_each_path = 'C:/Users/charlton/Desktop/MS_each.xlsx'
ms_each_df = pd.read_excel(ms_each_path)

# CSV 파일 경로
csv_paths = [
    'C:/Users/charlton/Desktop/Inventory_item/ct.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/mi.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/nj.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/ny.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/pa.CSV'
]

# 각 CSV 파일을 순회하며 병합
for csv_path in csv_paths:
    csv_df = pd.read_csv(csv_path)
    # 파일 이름을 기반으로 한 접미사 추가
    file_suffix = csv_path.split('/')[-1].split('.')[0]  # 파일 이름 추출
    csv_df.columns = [f"{col}_{file_suffix}" if col != 'Unnamed: 0' else 'ITEM' for col in csv_df.columns]

    # 병합하기
    ms_each_df = pd.merge(ms_each_df, csv_df, on='ITEM', how='left')

# 병합 결과 확인 및 저장
print(ms_each_df.head())
output_path = 'C:/Users/charlton/Desktop/xxxMerged_Data.xlsx'
ms_each_df.to_excel(output_path, index=False)
