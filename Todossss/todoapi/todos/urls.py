from django.urls import path
from . import views
from .views import todos, single_todo

urlpatterns = [
    path('',views.todos, name='todos'),
    path("<int:pk>/", single_todo, name="single_todo")
]