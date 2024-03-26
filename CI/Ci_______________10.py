import pandas as pd

# Excel 파일 경로
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

try:
    # 엑셀 파일의 모든 시트 이름 불러오기
    xl = pd.ExcelFile(excel_file)
    sheet_names = xl.sheet_names  # 모든 시트 이름을 저장
    print(f"Sheet Names: {sheet_names}")  # 시트 이름 출력

    # 'INVOICE' 시트에서 B16:G 범위의 데이터를 읽어오기
    df_filtered = pd.read_excel(excel_file, sheet_name='INVOICE', skiprows=15, usecols='B:G')

    # 결과를 새 Excel 파일로 저장
    output_file = r'C:\Users\charlton\Desktop\CI\filtered_data.xlsx'
    df_filtered.to_excel(output_file, index=False)
    print("데이터가 성공적으로 저장되었습니다:", output_file)

    # 첫 번째 시트의 데이터를 다시 불러와서 기본 정보 출력
    df_first_sheet = pd.read_excel(excel_file, sheet_name=sheet_names[0])

    # 데이터프레임의 구조 출력
    print("\nFirst Sheet Structure:")
    print("Columns:", df_first_sheet.columns.tolist())
    print("Data Types:\n", df_first_sheet.dtypes)
    print("Missing Values:\n", df_first_sheet.isnull().sum())
    print("First 5 Rows:\n", df_first_sheet.head())

except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")
