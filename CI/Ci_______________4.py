import pandas as pd

# 엑셀 파일 경로 설정
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

try:
    # 엑셀 파일의 모든 시트 이름 불러오기
    xl = pd.ExcelFile(excel_file)
    sheet_names = xl.sheet_names  # 모든 시트 이름을 저장
    print(f"Sheet Names: {sheet_names}")  # 시트 이름 출력

    # 첫 번째 시트를 기본으로 엑셀 파일 읽기
    df = pd.read_excel(excel_file, sheet_name=sheet_names[0])  # 첫 번째 시트 사용

    # 데이터프레임의 구조 출력
    print("File Structure:")
    print("Columns:", df.columns.tolist())
    print("Data Types:\n", df.dtypes)
    print("Missing Values:\n", df.isnull().sum())
    print("First 5 Rows:\n", df.head())

    # 전체 데이터 출력하는 부분을 주석 처리
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")
