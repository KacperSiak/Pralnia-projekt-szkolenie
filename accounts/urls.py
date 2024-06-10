from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import main_page


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("main_page", main_page, name="main_page"),
]