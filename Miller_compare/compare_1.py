import pandas as pd



# 생략된 열 없이 모든 열을 출력하도록 설정
pd.set_option('display.max_columns', None)


# CSV 파일을 pandas 데이터프레임으로 읽기
INV = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\S174.CSV", encoding='ISO-8859-1')
IR = pd.read_csv("C:\\Users\\charlton\\Desktop\\test\\IR4699.CSV", encoding='ISO-8859-1')



df_inv = INV
df_ir = IR

print(df_inv.columns)
print(df_ir.columns)

# print(INV)
# print(IR)

# 'DataFrom' 컬럼 추가 및 데이터프레임 정렬, 그리고 각 지역별 데이터프레임을 Categorical 타입으로 변환

# 데이터프레임 정렬


# 원하는 열 순서 정의
# desired_column_order = ['Date', 'Num', 'Name', 'P. O. #', 'Debit', 'DataFrom']

# 데이터프레임의 열 순서를 원하는 순서로 재배치


# 엑셀 파일로 저장

    # 데이터프레임을 각각의 시트에 저장


    # 테두리 스타일과 열 너비를 설정
    # border_format = writer.book.add_format({'border': 1})

    # 각 시트별로 테두리와 열 너비 적용


# 프로세스 종료 메시지
print("Process finished with exit code 0")
