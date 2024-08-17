from django.urls import path
from . import views


urlpatterns = [
    path('', views.helloworld, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('update_user/', views.update_user, name='update_user'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<str:cat>/', views.category, name='category'),
    path('category/', views.category_summary, name='category_summary'),
    path('additional_info/', views.additional_info, name='additional_info'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
]