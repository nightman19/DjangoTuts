from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Post views
    # path('login/', views.user_login, name='login'),
    # path('login/', auth_views.LoginView.as_view(), name="login"), 
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('', views.dashboard, name="dashboard"),

    # #Chanage password urls
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    # #Reset password urls
    # path('pasword_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), "password_reset_confirm"),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
