from django.urls import path, include

from .views import AbilityView, AbilityGroupView, AbilityGroupWithAbilityView, SingleAbilityGroupWithAbilityView

urlpatterns = [
    path('/', AbilityView.as_view()),
    path('/group/', AbilityGroupView.as_view()),
    path('/group-with-ability/', AbilityGroupWithAbilityView.as_view()),
    path('/group-with-ability/<int:pk>/', SingleAbilityGroupWithAbilityView.as_view()),
]