import pandas as pd

# CSV 파일을 pandas 데이터프레임으로 읽기
df_inv = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\S174.CSV", encoding='ISO-8859-1')
df_ir = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\IR4699.CSV", encoding='ISO-8859-1')

# 'Debit'와 'Credit'을 사용해 'Amount' 계산
df_inv['Amount'] = df_inv['Debit'] - df_inv['Credit']

# 필요한 열 선택
df_inv_selected = df_inv[['Item', 'Qty', 'Credit']]
df_ir_selected = df_ir[['Item', 'Qty', 'Amount']]

# 바탕화면 경로 설정
desktop_path = 'C:\\Users\\charlton\\Desktop\\output_excel.xlsx'

# 엑셀 파일로 저장
with pd.ExcelWriter(desktop_path, engine='openpyxl', mode='w') as writer:
    # 기존 데이터 및 요약 데이터 저장
    # (이전 코드와 동일한 부분은 생략)

    # INV 데이터에 대한 피벗 테이블 생성 및 저장
    inv_pivot = df_inv_selected.groupby('Item').sum().reset_index()
    inv_pivot.to_excel(writer, sheet_name='INV_VL', index=False)

    # IR 데이터에 대한 피벗 테이블 생성 및 저장
    ir_pivot = df_ir_selected.groupby('Item').sum().reset_index()
    ir_pivot.to_excel(writer, sheet_name='IR_VL', index=False)

# (이전 요약 데이터 및 중복 제거된 Item 목록 저장 코드는 여기에 포함됩니다)
