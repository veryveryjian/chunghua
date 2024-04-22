import pandas as pd
import os

# 출력 제한 해제
pd.set_option('display.max_rows', None)  # 행 제한 해제
pd.set_option('display.max_columns', None)  # 열 제한 해제
pd.set_option('display.width', None)  # 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 내용 너비 제한 해제

# 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI data2'
failed_files = []  # 실패한 파일들을 저장할 리스트
results = []  # 결과 데이터를 저장할 리스트

# 디렉터리 내의 모든 파일을 순회하면서 Excel 파일 찾기
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') and not filename.startswith('~$'):  # 임시 파일 제외
        file_path = os.path.join(directory, filename)
        try:
            print(f"\nProcessing file: {filename}")
            df = pd.read_excel(file_path, sheet_name='INVOICE', header=None)

            # 각 위치에 있는 값을 출력하고 저장
            result_data = {
                "Invoice NO.": df.iat[6, 6],
                "Loading date": df.iat[9, 1],
                "Ship date": df.iat[7, 6],
                "Voyage": df.iat[9, 6],
                "B/L NO.": df.iat[10, 6],
                "Container No.": df.iat[11, 6],
                "DataFrom": filename  # 파일 이름을 데이터 출처로 추가
            }

            # 'TOTAL' 문자열이 포함된 행 찾기
            total_row = df[df[0].str.contains('TOTAL', na=False, case=True)].index.tolist()
            if total_row:
                result_data["TOTAL"] = df.iat[total_row[0], 5]
                result_data["Qty"] = df.iat[total_row[0], 4]  # 새로운 컬럼 추가
            else:
                result_data["TOTAL"] = None
                result_data["Qty"] = None

            results.append(result_data)

        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            failed_files.append(filename)  # 실패한 파일명을 리스트에 추가

# 실패한 파일 목록 출력
if failed_files:
    print("\nFailed files:")
    for file in failed_files:
        print(file)

# 결과를 엑셀 파일에 저장
results_df = pd.DataFrame(results)
with pd.ExcelWriter(r'C:\Users\charlton\Desktop\Results.xlsx', engine='openpyxl') as writer:
    results_df.to_excel(writer, index=False)
