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
    path('department/', DepartmentView.as_view()),
    path('department/detail/<slug:slug>/', DepartmentDetailview.as_view()),
    path('designation/', DesignationView.as_view()),
    path('designation/detail/<slug:slug>/', DesignationDetailview.as_view()),
    path('classes/', MadrashaClassesView.as_view()),
    path('classes/detail/<slug:slug>/', MadrashaClassesDetailview.as_view()),
    path('group/', MadrashaClassGroupView.as_view()),
    path('group/detail/<slug:slug>/', MadrashaClassGroupDetailview.as_view()),
    path('shift/', ShiftView.as_view()),
    path('shift/detail/<slug:slug>/', ShiftDetailview.as_view()),
    path('session/', SessionView.as_view()),
    path('session/detail/<slug:slug>/', SessionDetailview.as_view()),

    path('books/', BooksView.as_view()),
    path('books/detail/<slug:slug>/', BooksDetailview.as_view()),

    path('<madrasha_slug>/fees/', FeesView.as_view()),
    path('fees/detail/<slug:slug>/', FeesDetailview.as_view()),

    path('exam-rules/', ExamRulesView.as_view()),
    path('exam-rules/detail/<slug:slug>/', ExamRulesDetailview.as_view()),

]
