import pandas as pd

# 엑셀 파일 경로 설정
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

try:
    # Excel 파일에서 모든 시트 이름 불러오기
    xl = pd.ExcelFile(excel_file)
    sheet_names = xl.sheet_names
    print("Available Sheets:", sheet_names)

    # 첫 번째 시트를 기본값으로 사용하거나, 특정 시트 이름을 지정할 수 있습니다.
    # 예제에서는 첫 번째 시트의 이름을 사용합니다.
    first_sheet_name = sheet_names[0]  # 첫 번째 시트 이름
    print(f"Reading Sheet: {first_sheet_name}")

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file, sheet_name=first_sheet_name)

    # 데이터프레임의 모든 정보 출력
    print("File Structure:")
    print("Columns:", df.columns.tolist())
    print("Data Types:\n", df.dtypes)
    print("Missing Values:\n", df.isnull().sum())
    print("First 5 Rows:\n", df.head())

    # 전체 데이터 출력
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")
