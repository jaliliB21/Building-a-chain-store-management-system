from django.urls import path


from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.detail, name='detail'),
    path('add_news/', views.add_news, name='add_news'),
    path('news/edit/<int:pk>/', views.edit, name='edit'),
    path('news/delete/<int:pk>/', views.delete, name='delete'),

]