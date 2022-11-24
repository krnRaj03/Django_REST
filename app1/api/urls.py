from django.urls import path
from app1.api import views

urlpatterns = [
    path('list/', views.movie_list, name="movie-list"),
    path('<int:pk>', views.movie_details, name="movie-details")
]
