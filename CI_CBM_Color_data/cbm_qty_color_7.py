import pandas as pd
import glob
import os

# 출력 제한 해제 설정
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 바탕화면의 'CI' 폴더 경로 설정
ci_folder_path = r'C:\Users\charlton\Desktop\CI data2\*.xlsx'

# CBM 엑셀 파일 경로 설정
cbm_file_path = r'C:\Users\charlton\Desktop\CBM.xlsx'
CBM_df = pd.read_excel(cbm_file_path)  # CBM 엑셀 파일 미리 읽어오기

# CI 폴더 내의 모든 엑셀 파일 처리
for excel_file in glob.glob(ci_folder_path):
    # Excel 파일 읽기
    df = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')
    Item_data = df[df['Item'].notna()]
    index_null_check = Item_data.dropna(subset=Item_data.columns[:6]).copy()

    # Item 분리
    split_data = index_null_check['Item'].str.split('-', n=1, expand=True)
    index_null_check['Color_code'] = split_data[0]
    index_null_check['spec_code'] = split_data[1]

    # 데이터 병합
    merged_df = pd.merge(index_null_check, CBM_df, on='spec_code', how='left')
    merged_df['cbmXqty'] = merged_df['CBM'] * merged_df['Pcs']

    # 결과 저장
    new_file_path = os.path.join(r'C:\Users\charlton\Desktop\test', os.path.basename(excel_file).replace('.xlsx', '_c.xlsx'))
    with pd.ExcelWriter(new_file_path, engine='xlsxwriter') as writer:
        merged_df.to_excel(writer, index=False, sheet_name='Joined Data')
        summary_df = merged_df.groupby('Color_code')['cbmXqty'].sum().reset_index()
        summary_df.to_excel(writer, index=False, sheet_name='Summary by Color')

    # 'Summary by Color' 시트의 데이터를 프린트
    print_summary_df = pd.read_excel(new_file_path, sheet_name='Summary by Color')
    print(f"Summary by Color for {new_file_path}:")
    print(print_summary_df)

    print(f"Processed and saved: {new_file_path}")

print("All files have been processed.")
