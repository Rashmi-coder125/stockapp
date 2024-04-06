from django.urls import path
from .views import home,item_list, add_item, edit_item, delete_item, add_category, delete_item_confirm, update_category
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='stockapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    path('item_list/', item_list, name='item_list'),
    path('add/', add_item, name='add_item'),
    path('edit/<int:pk>/', edit_item, name='edit_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
    path('add_category/', add_category, name='add_category'),
    path('delete_item_confirm/<int:pk>/', delete_item_confirm, name='delete_item_confirm'),
    path('update_category/<int:pk>/', update_category, name='update_category'),
]