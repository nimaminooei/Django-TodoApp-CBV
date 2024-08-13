from . import views
from django.urls import path,include
app_name  = 'accounts'

# from django.contrib.auth.views import LogoutView
from . import views
urlpatterns =[
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("login/", views.loginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    # djoser Token & JWT
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
]