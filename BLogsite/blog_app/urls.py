from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<str:slug>/',
         views.post_detail,
         name='post_detail'),
]
