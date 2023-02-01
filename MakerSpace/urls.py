from django.urls import path
from . import views  #引用這個資料夾中的views檔案
urlpatterns = [
    path('', views.index, name = "MakerSpace") #第二個參數需設定views.py中的檢視函式(View Function)名稱(index)
]