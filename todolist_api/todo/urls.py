from django.urls import path, include

from .views import TodoRetrieveUpdateView ,TodoRetrieveDeleteView, TodoView 
urlpatterns = [
    path('/', TodoView.as_view()),
    path('/<int:pk>', TodoRetrieveDeleteView.as_view()),
    path('/update/<int:pk>', TodoRetrieveUpdateView.as_view()),
    
]