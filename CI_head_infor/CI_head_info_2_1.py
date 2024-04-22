import pandas as pd

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제


# 파일 경로 설정
file_path = r'C:\Users\charlton\Desktop\CI data\PO#127E2  INVOICE（TGBU8731413）.xlsx'

# Excel 파일 읽기
try:
    # 'INVOICE' 시트 읽기, 처음 16행만 읽어오기, 헤더 없이
    df = pd.read_excel(file_path, sheet_name='INVOICE', header=None, nrows=16)

    # 데이터 프레임의 모든 행과 열을 출력
    print(df)
except Exception as e:
    print(f"파일을 읽는 데 실패했습니다: {e}")
