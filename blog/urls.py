from django.urls import path
from . import views

urlpatterns = [#IP주소/blog/
    path('', views.PostList.as_view()), #PostList = class명
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('category/<str:slug>/', views.category_page), #IP주소/ blog/category/slug/
    path('tag/<str:slug>/', views.tag_page),#IP주소/ blog/tag/slug/
    path('search/<str:q>/', views.PostSearch.as_view()),

    #path('', views.index),  #IP주소/blog #index는 함수 이름(사용자 지정 가능), views.py에 동일한 함수 이름이 있어야 함
    #path('<int:pk>/', views.single_post_page)
]