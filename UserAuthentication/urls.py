from django.urls import path
from . import views

urlpatterns = [
    # Login view
    path('', views.login_view, name='login_page'),
    
    # Login / Logout API
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
