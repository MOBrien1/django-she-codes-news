from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('profile/', views.LoggedInUserView.as_view()),
]