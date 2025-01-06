from django.urls import path

from . import views

urlpatterns = [
    path('displayMovie/<int:movieID>/', views.displayMovie, name="displayMovie"),
    path('search_by_title/', views.title_search_project, name="title_search_project"),
    path('add_rating/<int:movieID>/', views.add_rating, name='add_rating'),
    
]
