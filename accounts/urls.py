from django.urls import path
from .views import (
    DistrictList,
    ThanaList,
    PostOfficeList,
    PostCodeList,
    AddressDetail,
    MadrashaView,
    MadrashaDetailView,
    MadrashaDetail,
    MadrashaList
)

urlpatterns = [
    path('district/', DistrictList.as_view()),
    path('thana/', ThanaList.as_view()),
    path('post-office/', PostOfficeList.as_view()),
    path('post-code/', PostCodeList.as_view()),

    path('address/<int:pk>/', AddressDetail.as_view()),
    path('madrasha/', MadrashaView.as_view()),
    # path('madrasha/detail/<slug:slug>/', MadrashaDetailView.as_view()),
    path('madrasha/data/<slug:slug>/', MadrashaDetail.as_view()),
    path('madrasha-list/', MadrashaList.as_view()),
]