import os
import pandas as pd

# 출력 제한 해제
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 읽어올 파일들이 있는 디렉터리 설정
directory = r'C:\Users\charlton\Desktop\CI data2'

# 결과 데이터를 저장할 리스트 초기화
results = []

# 디렉터리 내의 모든 Excel 파일 이름을 리스트로 저장
excel_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]

# 각 Excel 파일을 순회하며 처리
for file in excel_files:
    file_path = os.path.join(directory, file)

    # 파일에서 데이터 읽기, 명시적으로 openpyxl 엔진 사용
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        print(f"Failed to read {file} with error: {e}")
        continue

    # 'TOTAL' 문자열이 일부분으로 포함된 행 찾기
    total_rows = df[df.iloc[:, 0].str.contains("TOTAL", na=False, case=True)]

    if not total_rows.empty:
        # 각 'TOTAL' 행의 5번 컬럼 값 추출 및 결과 저장
        for index, total_row in total_rows.iterrows():
            total_value = total_row.iloc[5]
            results.append({
                "파일 이름": file,
                "행 번호": index,
                "총액": total_value
            })
            print(f"파일: {file}, 행: {index}, 총액: {total_value}")

# 결과 데이터를 DataFrame으로 변환
results_df = pd.DataFrame(results)

# 결과를 Excel 파일로 저장
output_path = r'C:\Users\charlton\Desktop\CI_Total_list.xlsx'
results_df.to_excel(output_path, index=False)

# 저장된 파일 경로 출력
print(f"결과가 저장된 파일: {output_path}")
