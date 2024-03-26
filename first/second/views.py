from django.shortcuts import render
from django.http import HttpResponse
from .models import Cbm  # Cbm 모델을 임포트합니다.
from django.db import connection
from .forms import ExcelForm
from .models import ExcelFile
import pandas as pd
from .models import Item
from django.shortcuts import render, redirect
from .forms import ExcelForm
from .models import ExcelFile, Item  # Item 모델도 임포트합니다.
import logging  # 추가
from .models import Item  # Item 모델을 import 해야 합니다.
from django.db.models import F, Value
from django.db.models.functions import Concat
from .models import Item, Cbm
from django.shortcuts import render
from django.views.generic import ListView
from .models import Msavg
from django.shortcuts import render
from .models import Item, Msavg, MsRoom
from django.db.models import F

def cbm21(request):
    items_data = []

    # color_code가 "MS"로 시작하는 Item 객체만 조회합니다.
    for item in Item.objects.filter(color_code__startswith='MS'):
        msavg_data = Msavg.objects.filter(item=item.name).first()
        msroom_data = MsRoom.objects.filter(item=item.name).first()

        item_data = {
            'item_name': item.name,
            'on_hand': item.on_hand,
            'color_code': item.color_code,
            'model_code': item.model_code,
            'msavg_avg_2022': msavg_data.avg_2022 if msavg_data else "No Data",
            'msroom_details': {
                'model_code': msroom_data.model_code if msroom_data else "No Data",
                'ny': msroom_data.ny if msroom_data else "No Data",
                'nj': msroom_data.nj if msroom_data else "No Data",
                'ct': msroom_data.ct if msroom_data else "No Data",
                'pa': msroom_data.pa if msroom_data else "No Data",
                'number_275': msroom_data.number_275 if msroom_data else "No Data",
                'total': msroom_data.total if msroom_data else "No Data",
            },
        }

        items_data.append(item_data)

    context = {
        'items_data': items_data,
    }
    return render(request, 'pages/cbm21.html', context)





class MsavgListView(ListView):
    model = Msavg
    template_name = 'pages/msavg.html'  # 템플릿 파일 지정






def index(request):
    return render(request, 'pages/index.html')



from django.http import HttpResponse
from openpyxl import Workbook


def download_excel(request):
    color_code = request.GET.get('color_code', '')

    if color_code:
        items = Item.objects.filter(color_code=color_code)
    else:
        items = Item.objects.all()

    # 데이터 프레임을 생성하기 위한 준비
    data = []
    for item in items:
        # Cbm 모델에서 item의 model_code에 해당하는 cbm 값을 찾습니다.
        try:
            cbm_instance = Cbm.objects.get(model_code=item.model_code)
            cbm_value = cbm_instance.cbm
        except Cbm.DoesNotExist:
            cbm_value = "Not Found"

        data.append({
            'name': item.name,
            'on_hand': item.on_hand,
            'color_code': item.color_code,
            'model_code': item.model_code,
            'cbm': cbm_value,  # 여기에 cbm 값을 추가합니다.
        })

    # 준비된 데이터로부터 DataFrame을 생성합니다.
    df = pd.DataFrame(data)

    # 엑셀 파일로 변환
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="items_data.xlsx"'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response


#Color_code에 따른
def cbm(request):
    # 선택된 색상 코드를 가져옵니다.
    selected_color = request.GET.get('color_code', '')

    # 고유 색상 코드 목록을 생성합니다.
    unique_colors = Item.objects.values_list('color_code', flat=True).distinct()

    # 선택된 색상 코드에 따라 아이템을 필터링합니다.
    query = Item.objects.all()
    if selected_color:
        query = query.filter(color_code=selected_color)

    items_data = []
    for item in query:
        if item.on_hand == 0:
            continue

        try:
            cbm_instance = Cbm.objects.get(model_code=item.model_code)
            cbm_value = cbm_instance.cbm
            total_cbm = item.on_hand * cbm_value if cbm_value != "Not Found" else "Not Available"
        except Cbm.DoesNotExist:
            cbm_value = "Not Found"
            total_cbm = "Not Available"

        items_data.append({
            'item_name': item.name,
            'on_hand': item.on_hand,
            'cbm': cbm_value,
            'total_cbm': total_cbm,
        })

    context = {
        'items_data': items_data,
        'unique_colors': unique_colors,
        'selected_color': selected_color
    }
    return render(request, 'pages/cbm.html', context)





# 만약에 내가 item.on_hand 의 값이 0인 데이터는 미리 값을 제외하고
# total_cbm에는 0이 아닌 값만 데이터를 넘겨주고 싶다면?

# def cbm(request):
#     items_data = []
#     for item in Item.objects.all():
#         # item.on_hand 값이 0이면, 루프의 다음 반복으로 넘어갑니다.
#         if item.on_hand == 0:
#             continue
#
#         try:
#             cbm_instance = Cbm.objects.get(model_code=item.model_code)
#             cbm_value = cbm_instance.cbm
#             # 'cbm_value'가 "Not Found"가 아닌 실제 숫자일 때만 곱셈 연산 수행
#             # 여기서 item.on_hand 값이 0인 경우는 이미 위에서 걸러졌으므로 제외됩니다.
#             total_cbm = item.on_hand * cbm_value if cbm_value != "Not Found" else "Not Available"
#         except Cbm.DoesNotExist:
#             cbm_value = "Not Found"
#             total_cbm = "Not Available"
#
#         items_data.append({
#             'item_name': item.name,
#             # 'model_code': item.model_code, (주석 처리된 부분은 요구사항에 따라 제외하거나 포함시킬 수 있습니다.)
#             'on_hand': item.on_hand,
#             # 'color_code': item.color_code, (주석 처리된 부분은 요구사항에 따라 제외하거나 포함시킬 수 있습니다.)
#             # 'model_code': item.model_code, (주석 처리된 부분은 요구사항에 따라 제외하거나 포함시킬 수 있습니다.)
#             'cbm': cbm_value,
#             'total_cbm': total_cbm,  # 새로운 열에 해당하는 값 추가
#         })
#
#     context = {'items_data': items_data}
#     return render(request, 'pages/cbm.html', context)






# def cbm(request):
#     items_data = []
#     for item in Item.objects.all():
#         try:
#             cbm_instance = Cbm.objects.get(model_code=item.model_code)
#             cbm_value = cbm_instance.cbm
#             # 'cbm_value'가 "Not Found"가 아닌 실제 숫자일 때만 곱셈 연산 수행
#             total_cbm = item.on_hand * cbm_value if cbm_value != "Not Found" else "Not Available"
#         except Cbm.DoesNotExist:
#             cbm_value = "Not Found"
#             total_cbm = "Not Available"
#
#         items_data.append({
#             'item_name': item.name,
#             # 'model_code': item.model_code,
#             'on_hand': item.on_hand,
#             # 'color_code': item.color_code,
#             # 'model_code': item.model_code,
#             'cbm': cbm_value,
#             'total_cbm': total_cbm,  # 새로운 열에 해당하는 값 추가
#         })
#
#     context = {'items_data': items_data}
#     return render(request, 'pages/cbm.html', context)



# def cbm(request):
#     items_data = []
#     for item in Item.objects.all():
#         try:
#             cbm_instance = Cbm.objects.get(model_code=item.model_code)
#             cbm_value = cbm_instance.cbm
#         except Cbm.DoesNotExist:
#             cbm_value = "Not Found"
#
#         items_data.append({
#             'item_name': item.name,
#             'model_code': item.model_code,
#             'on_hand': item.on_hand,
#             'color_code': item.color_code,
#             'model_code': item.model_code,
#             'cbm': cbm_value,
#
#         })
#
#     context = {'items_data': items_data}
#     return render(request, 'pages/cbm.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # logger.debug(f"File uploaded: {instance.file.name}")

            file_type = instance.file.name.split('.')[-1].lower()
            if file_type in ['xlsx', 'xls', 'csv']:
                df = pd.read_excel(instance.file.path) if file_type in ['xlsx', 'xls'] else pd.read_csv(
                    instance.file.path)

                # 데이터베이스에서 기존 데이터 삭제
                Item.objects.all().delete()

                # 'Unnamed: 0' 열을 '-' 기호를 기준으로 분리
                split_data = df['Unnamed: 0'].str.split('-',n=1, expand=True).fillna('')
                df['Color_Code'] = split_data[0]
                df['Model_Code'] = split_data[1]

                # 새로운 데이터 업로드
                for _, row in df.iterrows():
                    Item.objects.create(
                        name=row['Unnamed: 0'],
                        on_hand=row['On Hand'],
                        color_code=row['Color_Code'],
                        model_code=row['Model_Code']
                    )

                return redirect('item_list')
            else:
                instance.delete()
                return render(request, 'pages/upload.html', {'form': form, 'error': 'Unsupported file format.'})
        else:
            return render(request, 'pages/upload.html', {'form': form})
    else:
        form = ExcelForm()
    return render(request, 'pages/upload.html', {'form': form})



from django.db.models import F, Value
from django.db.models.functions import Concat
from .models import Item, Cbm

# 'Item' 모델의 인스턴스를 반복하면서 각 인스턴스에 해당하는 'Cbm' 모델의 'cbm' 값을 가져옵니다.
# for item in Item.objects.all():
#     try:
#         cbm_instance = Cbm.objects.get(model_code=item.model_code)
#         print(f"Item: {item.name}, Model Code: {item.model_code}, CBM: {cbm_instance.cbm}")
#     except Cbm.DoesNotExist:
#         print(f"Item: {item.name}, Model Code: {item.model_code}, CBM: Not Found")
#






# def upload_file(request):
#     if request.method == 'POST':
#         form = ExcelForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save()
#             logger.debug(f"File uploaded: {instance.file.name}")
#
#             file_type = instance.file.name.split('.')[-1].lower()
#             if file_type in ['xlsx', 'xls', 'csv']:
#                 df = pd.read_excel(instance.file.path) if file_type in ['xlsx', 'xls'] else pd.read_csv(
#                     instance.file.path)
#
#                 # 'Unnamed: 0' 열을 '-' 기호를 기준으로 분리
#                 split_data = df['Unnamed: 0'].str.split('-', expand=True).fillna('')
#                 df['Color_Code'] = split_data[0]
#                 df['Model_Code'] = split_data[1]
#
#                 # 데이터베이스에 데이터 저장
#                 for _, row in df.iterrows():
#                     Item.objects.create(
#                         name=row['Unnamed: 0'],
#                         on_hand=row['On Hand'],
#                         color_code=row['Color_Code'],
#                         model_code=row['Model_Code']
#                     )
#
#                 return redirect('item_list')
#             else:
#                 instance.delete()
#                 return render(request, 'pages/upload.html', {'form': form, 'error': 'Unsupported file format.'})
#         else:
#             return render(request, 'pages/upload.html', {'form': form})
#     else:
#         form = ExcelForm()
#     return render(request, 'pages/upload.html', {'form': form})
#
#
#
def item_list(request):
    items = Item.objects.all()
    return render(request, 'pages/item_list.html', {'items': items})



def hi(request):
    cbm_data = Cbm.objects.all()  # Cbm 모델의 모든 데이터를 가져옵니다.
    context = {'cbm_data': cbm_data}  # 템플릿에 전달할 데이터를 context 딕셔너리에 추가합니다.
    return render(request, 'pages/hey.html', context)  # context를 함께 템플릿에 전달합니다.


from django.shortcuts import render, redirect
from .forms import ExcelForm
import pandas as pd

# 로거 설정
# logger = logging.getLogger(__name__)


# def upload_file(request):
#     if request.method == 'POST':
#         form = ExcelForm(request.POST, request.FILES)
#         if form.is_valid():
#             logger.debug("Form is valid.")
#             instance = form.save()
#             logger.debug(f"File uploaded: {instance.file.name}")
#
#             file_type = instance.file.name.split('.')[-1].lower()
#             if file_type in ['xlsx', 'xls', 'csv']:
#                 logger.debug(f"Processing {file_type} file.")
#                 # 파일 타입에 따라 적절한 pandas 함수 호출
#                 if file_type in ['xlsx', 'xls']:
#                     df = pd.read_excel(instance.file.path)
#                 else:
#                     df = pd.read_csv(instance.file.path)
#                 logger.debug("DataFrame loaded.")
#                 logger.debug(df.head())  # 데이터프레임의 첫 5행 출력
#
#                 # 데이터베이스에 데이터 저장
#                 for _, row in df.iterrows():
#                     Item.objects.create(name=row['Unnamed: 0'], on_hand=row['On Hand'])
#                 logger.debug("Data saved to database.")
#
#                 return redirect('item_list')
#             else:
#                 instance.delete()
#                 logger.error("Unsupported file format.")
#                 return render(request, 'pages/upload.html', {'form': form, 'error': 'Unsupported file format.'})
#         else:
#             logger.error("Form is not valid.")
#     else:
#         form = ExcelForm()
#     return render(request, 'pages/upload.html', {'form': form})

# def index(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT model_code, cbm FROM cbm")  # Raw SQL 쿼리 실행
#         cbm_data = cursor.fetchall()  # 결과 가져오기
#
#     # 결과를 'cbm_data' 키와 함께 context에 추가
#     context = {'cbm_data': [{'model_code': row[0], 'cbm': row[1]} for row in cbm_data]}
#     return render(request, 'pages/hey.html', context)


# def index(request):
#
#     return HttpResponse("Hello World! You got it!")

# def index(request):
#     context = { }
#     # 3개의 인자를 받는다
#     # html은 ' ' 따옴표로, pages/ 바로 위치 적용하네
#     return render(request,'pages/hey.html',context)

