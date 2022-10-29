from django.urls import path
from .views import (
    DepartmentView,
    DepartmentDetailview,
    DesignationView,
    DesignationDetailview,
    MadrashaClassesView,
    MadrashaClassesDetailview,
    MadrashaClassGroupView,
    MadrashaClassGroupDetailview,
    ShiftView,
    ShiftDetailview,
    SessionView,
    SessionDetailview,
    BooksView,
    BooksDetailview,
    FeesView,
    FeesDetailview,
    ExamRulesView,
    ExamRulesDetailview
)

urlpatterns = [
    path('<str:madrasha_slug>/department/', DepartmentView.as_view()),
    path('department/detail/<int:pk>/', DepartmentDetailview.as_view()),

    path('<str:madrasha_slug>/designation/', DesignationView.as_view()),
    path('designation/detail/<int:pk>/', DesignationDetailview.as_view()),
    path('<str:madrasha_slug>/classes/', MadrashaClassesView.as_view()),
    path('classes/detail/<int:pk>/', MadrashaClassesDetailview.as_view()),

    path('<madrasha_slug>/group/', MadrashaClassGroupView.as_view()),
    path('group/detail/<int:pk>/', MadrashaClassGroupDetailview.as_view()),

    path('<madrasha_slug>/shift/', ShiftView.as_view()),
    path('shift/detail/<int:pk>/', ShiftDetailview.as_view()),

    path('<str:madrasha_slug>/session/', SessionView.as_view()),
    path('session/detail/<int:pk>/', SessionDetailview.as_view()),

    path('books/', BooksView.as_view()),
    path('<madrasha_slug>/books/', BooksView.as_view()),
    path('books/detail/<int:pk>/', BooksDetailview.as_view()),

    path('<madrasha_slug>/fees/', FeesView.as_view()),
    path('fees/detail/<int:pk>/', FeesDetailview.as_view()),

    path('exam-rules/', ExamRulesView.as_view()),
    path('exam-rules/detail/<int:pk>/', ExamRulesDetailview.as_view()),

]
