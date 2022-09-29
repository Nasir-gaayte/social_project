
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/singin.html')),
    path('logout/',auth_views.LogoutView.as_view(),name='loguot'),
    path('singup/',views.SingUp.as_view(),name='singup'),
]
