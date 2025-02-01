from django.urls import path
from .views import main
from . import views
from .views.main import register
urlpatterns = [
    
    path('home', main.home, name='home'),
    path('show/', main.ShowPageView.as_view(), name='show_page'),
    
    path('register/', register, name="register")
]