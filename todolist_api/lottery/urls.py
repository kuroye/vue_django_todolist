from django.urls import path

from .views import AllCardView, CardView, CardStockView

urlpatterns = [
    path('/all-card/', AllCardView.as_view()),
    path('/draw-card/', CardView.as_view()),
    path('/card-stock/', CardStockView.as_view()),
    # path('/group/', AbilityGroupView.as_view()),
    # path('/group-with-ability/', AbilityGroupWithAbilityView.as_view()),
    # path('/group-with-ability/<int:pk>/', SingleAbilityGroupWithAbilityView.as_view()),
]