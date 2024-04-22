import pandas as pd
import os

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI data'
failed_files = []  # 실패한 파일들을 저장할 리스트

# 디렉터리 내의 모든 파일을 순회하면서 Excel 파일 찾기
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') and not filename.startswith('~$'):  # 임시 파일 제외
        file_path = os.path.join(directory, filename)
        try:
            print(f"\nProcessing file: {filename}")
            df = pd.read_excel(file_path, sheet_name='INVOICE', header=None)

            # 출력할 값의 위치와 설명
            positions = [
                (6, 6, "Invoice NO."),
                (9, 1, "Loading date"),
                (7, 6, "Ship date"),
                (9, 6, "Voyage"),
                (10, 6, "B/L NO."),
                (11, 6, "Container No.")
            ]

            # 각 위치에 있는 값을 출력
            for row, col, title in positions:
                print(f"{title}: {df.iat[row, col]}")

            # 'TOTAL' 문자열이 포함된 행 찾기
            total_row = df[df[0].str.contains('TOTAL', na=False, case=True)].index.tolist()
            if total_row:
                for row in total_row:
                    total_value = df.iat[row, 5]
                    print(f"Row {row} - Total Amount: {total_value}")
            else:
                print("No 'TOTAL' string found in the first column.")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            failed_files.append(filename)  # 실패한 파일명을 리스트에 추가

# 실패한 파일 목록 출력
if failed_files:
    print("\nFailed files:")
    for file in failed_files:
        print(file)
