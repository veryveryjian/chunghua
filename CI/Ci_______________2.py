import pandas as pd

# 엑셀 파일 경로 설정
excel_file = r'C:\Users\charlton\Desktop\CI\PO#330MS  INVOICE（TCKU6328636）.xlsx'

try:
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file)

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
