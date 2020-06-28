from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('<int:post_id>/', views.detail, name='blog-detail'),
]