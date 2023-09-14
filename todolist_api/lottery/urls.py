from django.urls import path

from .views import CardView

urlpatterns = [
    path('/', CardView.as_view()),
    # path('/group/', AbilityGroupView.as_view()),
    # path('/group-with-ability/', AbilityGroupWithAbilityView.as_view()),
    # path('/group-with-ability/<int:pk>/', SingleAbilityGroupWithAbilityView.as_view()),
]