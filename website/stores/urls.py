from django.urls import path


from . import views

app_name = 'stores'

urlpatterns = [
    path('stores/', views.stores, name='stores'),
    path('add_store/', views.addin_store, name='add_store'),
    path('stores/edit/<int:pk>/', views.edit, name='edit'),
    path('stores/delete/<int:pk>/', views.delete, name='delete'),
]
