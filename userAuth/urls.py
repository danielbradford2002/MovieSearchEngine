from django.urls import path
from . import views
#from .views import SearchPageView

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='registration'),
]
