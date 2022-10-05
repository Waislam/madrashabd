from django.urls import path
from .views import (SubCategoryList,
                    ExpenseSubCategoryList,
                    StudentIncomeView,
                    StudentIncomeDetailView,
                    OtherIncomeView,
                    OtherIncomeDetailView, AllExpenseView, AllExpenseDetailView
                    )

urlpatterns = [
    path('sub-category/', SubCategoryList.as_view()),
    path('expense/sub-category/', ExpenseSubCategoryList.as_view()),
    path('student-income/', StudentIncomeView.as_view()),
    path('student-income/<int:pk>/', StudentIncomeDetailView.as_view()),
    path('<int:madrasha_slug>/other-income/', OtherIncomeView.as_view()),
    path('other-income/<int:pk>/', OtherIncomeDetailView.as_view()),
    path('expense/', AllExpenseView.as_view()),
    path('expense/<int:pk>/', AllExpenseDetailView.as_view()),
]
