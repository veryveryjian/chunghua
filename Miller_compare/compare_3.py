import pandas as pd

# CSV 파일을 pandas 데이터프레임으로 읽기
df_inv = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\S174.CSV", encoding='ISO-8859-1')
df_ir = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\IR4699.CSV", encoding='ISO-8859-1')

# 'Debit'와 'Credit'을 사용해 'Amount' 계산 (예시: 'Debit' - 'Credit')
df_inv['Amount'] = df_inv['Debit'] - df_inv['Credit']

# 필요한 열 선택 (INV에서는 'Credit'을 사용하여 'Amount' 대체)
df_inv_selected = df_inv[['Item', 'Qty', 'Credit']]
df_ir_selected = df_ir[['Item', 'Qty', 'Amount']]

# 바탕화면 경로 설정
desktop_path = 'C:\\Users\\charlton\\Desktop\\output_excel.xlsx'

# 각각의 Item 열의 개수와 Qty 열의 합계 계산
summary_data = pd.DataFrame({
    'Sheet': ['INV', 'IR'],
    'Item Count': [df_inv_selected['Item'].nunique(), df_ir_selected['Item'].nunique()],
    'Qty Sum': [df_inv_selected['Qty'].sum(), df_ir_selected['Qty'].sum()]
})

# 엑셀 파일로 저장
with pd.ExcelWriter(desktop_path, engine='openpyxl', mode='w') as writer:
    summary_data.to_excel(writer, sheet_name='Summary_rawData', index=False)
    df_inv_selected.to_excel(writer, sheet_name='INV_rawdata', index=False)
    df_ir_selected.to_excel(writer, sheet_name='IR_rawdata', index=False)
