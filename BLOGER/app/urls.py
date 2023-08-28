from . import views
from django.urls import path
urlpatterns=[
    path("",views.PostList.as_view(),name='home'),
    path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),
    path('create/', views.create_blog_post1.as_view(), name='create-blog-post'),
    
]