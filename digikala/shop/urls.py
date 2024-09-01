from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)


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
    path('', include(router.urls)),
]