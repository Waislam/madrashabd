from django.urls import path
from .views import (
    DivisionListView,
    DistrictListView,
    ThanaListView,
    PostOfficeListView,
    PostCodeListView,
    AddressDetail,
    MadrashaView,
    MadrashaDetailView,
    UserRegistrationView,
    CustomAuthToken,
    MadrashaUserListingView,
    AvatarUpdateView
)

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),

    # Address path
    path('district/', DistrictListView.as_view()),
    path('division/', DivisionListView.as_view()),
    path('thana/', ThanaListView.as_view()),
    path('post-office/', PostOfficeListView.as_view()),
    path('post-code/', PostCodeListView.as_view()),
    path('address/<int:pk>/', AddressDetail.as_view()),

    # madrasha path
    path('madrasha/', MadrashaView.as_view()),
    path('madrasha/detail/<slug:slug>/', MadrashaDetailView.as_view()),
    path('madrasha-admin/', UserRegistrationView.as_view()),
    path('mu-listing/', MadrashaUserListingView.as_view()),  # madrashauser listing
    path('avatar/<int:pk>/', AvatarUpdateView.as_view()),
]
