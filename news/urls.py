from django.urls import path
from . import views


app_name = 'news'


urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('category/<str:category>/', views.post_by_category, name='category'),
]