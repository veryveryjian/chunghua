import pandas as pd

# 기존 MS_each 엑셀 파일 불러오기
ny_test_file_path = 'C:/Users/charlton/Desktop/MS_each.xlsx'
MS_each = pd.read_excel(ny_test_file_path)

# CSV 파일 경로
csv_files = [
    'C:/Users/charlton/Desktop/Inventory_item/ct.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/mi.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/nj.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/ny.CSV',
    'C:/Users/charlton/Desktop/Inventory_item/pa.CSV'
]

# 각 CSV 파일을 순회하며 Unnamed: 0 열의 데이터를 병합
for file in csv_files:
    # 현재 CSV 파일 불러오기
    current_df = pd.read_csv(file)

    # 'Unnamed: 0' 열이 존재하는지 확인하고, 존재한다면 MS_each 데이터프레임과 병합
    if 'Unnamed: 0' in current_df.columns:
        # 병합 기준을 'Unnamed: 0'으로 설정하여 현재 CSV 파일의 데이터를 추가
        MS_each = pd.merge(MS_each, current_df[['Unnamed: 0']], left_on='ITEM', right_on='Unnamed: 0', how='left')

        # 현재 CSV 파일에서 가져온 'Unnamed: 0' 열을 적절한 이름으로 변경하여 구분
        new_column_name = f"Data_from_{file.split('/')[-1].split('.')[0]}"  # 예: Data_from_ct
        MS_each.rename(columns={'Unnamed: 0': new_column_name}, inplace=True)

# 결과를 새로운 엑셀 파일로 저장
output_file_path = 'C:/Users/charlton/Desktop/Updated_MS_each_r1.xlsx'
MS_each.to_excel(output_file_path, index=False)
