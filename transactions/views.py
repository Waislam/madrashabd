from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from .serializers import (IncomeSubCategorySerializer, StudentIncomeSerializer, OtherIncomeSerializer,
                          OtherIncomeListSerializer, StudentIncomeListSerializer, AllExpenseListSerializer,
                          AllExpenseSerializer)
from rest_framework.views import APIView
from .models import IncomeCategory, IncomeSubCategory, StudentIncome, ExpenseCategory, OtherIncome, AllExpense
from django.http.response import JsonResponse
from rest_framework import mixins, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import StudentIncomeFilter, OtherIncomeFilter, AllExpenseFilter
from students.pagination import CustomPagination


# Create your views here.


class SubCategoryList(APIView):
    def post(self, request):
        category = request.data['category']
        sub_cat = {}
        if category:
            sub_cats = IncomeCategory.objects.get(id=category).sub_categories.all()
            sub_cat = {d.name: d.id for d in sub_cats}
        return JsonResponse(data=sub_cat, safe=False)


class ExpenseSubCategoryList(APIView):
    def post(self, request):
        category = request.data['category']
        sub_cat = {}
        if category:
            sub_cats = ExpenseCategory.objects.get(id=category).expense_sub_cats.all()
            sub_cat = {d.name: d.id for d in sub_cats}
        return JsonResponse(data=sub_cat, safe=False)


class StudentIncomeView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = StudentIncome.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentIncomeFilter
    search_fields = ["student_class_id"]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentIncomeListSerializer
        return StudentIncomeSerializer

    def get(self, request, *args, **kwargs):
        """method to show the list of Income from Student"""
        # self.serializer_class = StudentListSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Income from student obj"""
        # self.serializer_class = StudentSerializer
        return self.create(request, *args, **kwargs)


class StudentIncomeDetailView(APIView):
    """this class is for CRUD"""

    def get_object(self, pk):
        """For getting single obj with slug field"""
        try:
            return StudentIncome.objects.get(id=pk)
        except StudentIncome.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        """For getting single object details"""
        student_income = self.get_object(pk)
        serializer = StudentIncomeListSerializer(student_income)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        """update single obj details"""
        student_income = self.get_object(pk)
        serializer = StudentIncomeSerializer(student_income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Student Income has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response(
            {"status": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class OtherIncomeView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = OtherIncome.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = OtherIncomeFilter
    search_fields = ["receipt_book_number"]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OtherIncomeListSerializer
        return OtherIncomeSerializer

    def get(self, request, *args, **kwargs):
        """method to show the list of Income from Student"""
        # self.serializer_class = StudentListSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Income from student obj"""
        # self.serializer_class = StudentSerializer
        return self.create(request, *args, **kwargs)


class OtherIncomeDetailView(APIView):
    """this class is for CRUD"""

    def get_object(self, pk):
        """For getting single obj with slug field"""
        try:
            return OtherIncome.objects.get(id=pk)
        except OtherIncome.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        """For getting single object details"""
        other_income = self.get_object(pk)
        serializer = OtherIncomeListSerializer(other_income)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        """update single obj details"""
        other_income = self.get_object(pk)
        serializer = OtherIncomeSerializer(other_income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Other Income has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response(
            {"status": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class AllExpenseView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = AllExpense.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AllExpenseFilter
    search_fields = ["voucher_name"]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AllExpenseListSerializer
        return AllExpenseSerializer

    def get(self, request, *args, **kwargs):
        """method to show the list of Income from Student"""
        # self.serializer_class = StudentListSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Income from student obj"""
        # self.serializer_class = StudentSerializer
        return self.create(request, *args, **kwargs)


class AllExpenseDetailView(APIView):
    """this class is for CRUD"""

    def get_object(self, pk):
        """For getting single obj with slug field"""
        try:
            return AllExpense.objects.get(id=pk)
        except AllExpense.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        """For getting single object details"""
        all_expense = self.get_object(pk)
        serializer = AllExpenseListSerializer(all_expense)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        """update single obj details"""
        all_expense = self.get_object(pk)
        serializer = AllExpenseSerializer(all_expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Expense has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response(
            {"status": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )