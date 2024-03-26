import pandas as pd

# CSV 파일을 pandas 데이터프레임으로 읽기
df_inv = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\S174.CSV", encoding='ISO-8859-1')
df_ir = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\IR4699.CSV", encoding='ISO-8859-1')

# 'Debit'와 'Credit'을 사용해 'Amount' 계산
df_inv['Amount'] = df_inv['Debit'] - df_inv['Credit']

# 필요한 열 선택
df_inv_selected = df_inv[['Item', 'Qty', 'Credit']]
df_ir_selected = df_ir[['Item', 'Qty', 'Amount']]

# 중복 포함된 Item 열의 전체 개수 계산
inv_item_count_total = df_inv_selected['Item'].count()
ir_item_count_total = df_ir_selected['Item'].count()

# 중복 제거 후 Item 열의 개수 계산
inv_item_count_deduplicated = df_inv_selected['Item'].drop_duplicates().count()
ir_item_count_deduplicated = df_ir_selected['Item'].drop_duplicates().count()

# 중복 제거된 Item 목록
df_inv_items_deduplicated = df_inv_selected[['Item']].drop_duplicates()
df_ir_items_deduplicated = df_ir_selected[['Item']].drop_duplicates()

# 바탕화면 경로 설정
desktop_path = 'C:\\Users\\charlton\\Desktop\\output_excel.xlsx'

# 엑셀 파일로 저장
with pd.ExcelWriter(desktop_path, engine='openpyxl', mode='w') as writer:
    # 요약 데이터 추가
    summary_data = pd.DataFrame({
        'Sheet': ['INV', 'IR'],
        'Item Count': [inv_item_count_total, ir_item_count_total],  # 중복 포함한 전체 Item 수
        'Qty Sum': [df_inv_selected['Qty'].sum(), df_ir_selected['Qty'].sum()],
        'Deduplicated Item Count': [inv_item_count_deduplicated, ir_item_count_deduplicated]  # 중복 제거 후 Item 카운트
    })
    summary_data.to_excel(writer, sheet_name='Summary', index=False)

    # 원본 데이터 저장
    df_inv_selected.to_excel(writer, sheet_name='INV_rawdata', index=False)
    df_ir_selected.to_excel(writer, sheet_name='IR_rawdata', index=False)

    # 중복 제거된 Item 목록 저장
    df_inv_items_deduplicated.to_excel(writer, sheet_name='INV_Item_duplicated_check', index=False)
    df_ir_items_deduplicated.to_excel(writer, sheet_name='IR_Item_duplicated_check', index=False)

    # INV 데이터에 대한 피벗 테이블 생성 및 저장
    inv_pivot = df_inv_selected.groupby('Item').agg({'Qty': 'sum', 'Credit': 'sum'}).reset_index()
    inv_pivot.to_excel(writer, sheet_name='INV_VL', index=False)

    # IR 데이터에 대한 피벗 테이블 생성 및 저장
    ir_pivot = df_ir_selected.groupby('Item').agg({'Qty': 'sum', 'Amount': 'sum'}).reset_index()
    ir_pivot.to_excel(writer, sheet_name='IR_VL', index=False)
