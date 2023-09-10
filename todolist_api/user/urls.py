from django.urls import path

from .views import UserCreateAPIView, UserRetrieveAPIView, UserDoDoUpdateAPIView
from ability.views import UserAbilityUpdateAPIView

urlpatterns = [
    path('/register', UserCreateAPIView.as_view()),
    path('/<int:pk>', UserRetrieveAPIView.as_view()),
    path('/dodo', UserDoDoUpdateAPIView.as_view()),
    path('/ability', UserAbilityUpdateAPIView.as_view()),
    # path('/update/<int:pk>', TodoRetrieveUpdateView.as_view()),
    
]