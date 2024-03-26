from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from second import views
from second.views import item_list
from second.views import cbm
from second.views import download_excel  # download_excel 뷰 함수를 가져옵니다.
from second.views import MsavgListView
from second.views import cbm21



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hi', views.hi, name='home'),  # Ensure this pattern is defined for the root URL
    path('upload/', views.upload_file, name='upload_file'),
    path('items/', item_list, name='item_list'),
    path('cbm/', cbm, name='cbm'),
    path('ex/', download_excel, name='download_excel'),  # download_excel 뷰를 추가
    path('msavg/', MsavgListView.as_view(), name='msavg-list'),
    path('cbm21/', cbm21, name='cbm21'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
