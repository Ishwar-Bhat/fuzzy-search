from django.urls import path
from . import views

urlpatterns = [
    path('words/', views.add_words, name="add_words")
]
