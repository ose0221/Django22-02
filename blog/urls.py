from django.urls import path
from . import views
urlpatterns = [#IP주소/blog
    path('', views.index),  #IP주소/blog #index는 함수 이름(사용자 지정 가능), views.py에 동일한 함수 이름이 있어야 함
    path('<int:pk>/', views.single_post_page)
]