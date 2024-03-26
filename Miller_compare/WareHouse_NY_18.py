import pandas as pd

# MS_each 엑셀 파일 불러오기
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

# 각 CSV 파일을 순회하며 "On Hand" 데이터 병합
for csv_path in csv_paths:
    # CSV 파일 불러오기
    csv_df = pd.read_csv(csv_path)

    # 필요한 컬럼만 선택 ("Unnamed: 0" 및 "On Hand")
    csv_df_filtered = csv_df[['Unnamed: 0', 'On Hand']].copy()

    # "Unnamed: 0" 컬럼명을 "ITEM"으로 변경
    csv_df_filtered.rename(columns={'Unnamed: 0': 'ITEM'}, inplace=True)

    # 병합하기 (ITEM 컬럼을 기준으로)
    ms_each_df = pd.merge(ms_each_df, csv_df_filtered, on='ITEM', how='left',
                          suffixes=('', '_from_' + csv_path.split('/')[-1].split('.')[0]))

# 병합된 데이터 확인 및 저장
print(ms_each_df.head())
output_path = 'C:/Users/charlton/Desktop/F_1.xlsx'
ms_each_df.to_excel(output_path, index=False)




