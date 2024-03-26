import pandas as pd

# 파일 경로
file_path = 'C:/Users/charlton/Desktop/Ny_sim2.xlsx'

# 데이터 불러오기
df = pd.read_excel(file_path)

# 필요한 경우 추가적인 데이터 처리 수행



from django.shortcuts import render

# 앞서 정의한 pandas 코드 포함

def display_inventory(request):
    # 파일에서 데이터 불러오기 및 처리 코드

    # 데이터를 템플릿으로 전달
    context = {
        'inventory_data': df.to_dict('records')  # DataFrame을 딕셔너리 리스트로 변환
    }
    return render(request, 'test.html', context)
