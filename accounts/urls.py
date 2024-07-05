from django.urls import path

from .views import UserRegistrationView,UserLoginView,LogoutView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='user_registration'),
    path('logout/',LogoutView.as_view(),name='user_logout'),
    path('login/',UserLoginView.as_view(),name='user_login')
]
