"""
1. Department
2. Designation
3. MadrashaClasses
4. MadrashaClassesGroup
5. Shift
6. Books
7. Fees
8. Session
9. Exam rules
"""
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Designation, MadrashaClasses, MadrashaGroup, Shift, Session, Books, ExamRules, Fees
from .serializers import (DepartmentSerializer, DesignationSerializer, ClassSerializer, ClassGroupSerializer,
                          ShiftSerializer,
                          BooksSerializer, SessionSerializer, ExamRulesSerializer,
                          FeesSerializer)
from .serializers import (DepartmentListSerializer,
                          DesignationListSerializer,
                          ClassListSerializer,
                          BooksListSerializer,
                          SessionListSerializer,
                          ClassGroupListSerializer,
                          ShiftListSerializer,
                          FeesListSerializer
                          )


# Create your views here.

# ========================== 1. Department ===================================


class DepartmentView(APIView):
    """ A class to creae api for Department """

    def post(self, request, formate=None, **kwargs):
        """creating department object"""
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, **kwargs):
        """ showing a list of depatment objects"""
        department = Department.objects.filter(madrasha__slug=madrasha_slug)
        serializer = DepartmentListSerializer(department, many=True)
        return Response(serializer.data)


class DepartmentDetailview(APIView):
    """ department detail, update and delete"""

    def get_object(self, slug):
        """get single department obj"""
        try:
            return Department.objects.get(slug=slug)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        department = self.get_object(slug)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        department = self.get_object(slug)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """delete"""
        department = self.get_object(slug)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ========================== 2. Designation ===================================


class DesignationView(APIView):
    """ A class to create api for Designation """

    def post(self, request, formate=None, **kwargs):
        """creating Designation object"""
        serializer = DesignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of Designation objects"""
        designations = Designation.objects.filter(madrasha__slug=madrasha_slug)
        serializer = DesignationListSerializer(designations, many=True)
        return Response(serializer.data)


class DesignationDetailview(APIView):
    """ Designation detail, update and delete"""

    def get_object(self, slug):
        """get single Designation obj"""
        try:
            return Designation.objects.get(slug=slug)
        except Designation.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details view for single obj"""
        designation = self.get_object(slug)
        serializer = DesignationSerializer(designation)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        designation = self.get_object(slug)
        serializer = DesignationSerializer(designation, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """delete"""
        designation = self.get_object(slug)
        designation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ========================== 3.MadrashaClasses ===================================


class MadrashaClassesView(APIView):
    """ A class to create api for MadrashaClasses """

    def post(self, request, formate=None, **kwargs):
        """creating MadrashaClasses object"""
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of MadrashaClasses objects"""
        classes = MadrashaClasses.objects.filter(madrasha__slug=madrasha_slug)
        serializer = ClassListSerializer(classes, many=True)
        return Response(serializer.data)


class MadrashaClassesDetailview(APIView):
    """ MadrashaClasses detail, update and delete"""

    def get_object(self, slug):
        """get single MadrashaClasses obj"""
        try:
            return MadrashaClasses.objects.get(slug=slug)
        except MadrashaClasses.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        madrashaclass = self.get_object(slug)
        serializer = ClassSerializer(madrashaclass)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        madrashaclass = self.get_object(slug)
        serializer = ClassSerializer(madrashaclass, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """delete"""
        madrashaclass = self.get_object(slug)
        madrashaclass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================ 4. MadrashaClassesGroup =======================================

class MadrashaClassGroupView(APIView):
    """ A class to create api for MadrashaClassesGroup """

    def post(self, request, formate=None, **kwargs):
        """creating department object"""
        serializer = ClassGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of MadrashaClassesGroup objects"""
        groups = MadrashaGroup.objects.filter(madrasha__slug=madrasha_slug)
        serializer = ClassGroupListSerializer(groups, many=True)
        return Response(serializer.data)


class MadrashaClassGroupDetailview(APIView):
    """ MadrashaClassesGroup detail, update and delete"""

    def get_object(self, slug):
        """get single MadrashaClassesGroup obj"""
        try:
            return MadrashaGroup.objects.get(slug=slug)
        except MadrashaGroup.DoesNotExist:
            return Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        madrashagroup = self.get_object(slug)
        serializer = ClassGroupSerializer(madrashagroup)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        madrashagroup = self.get_object(slug)
        serializer = ClassGroupSerializer(madrashagroup, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """delete"""
        madrashagroup = self.get_object(slug)
        madrashagroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================== 5. Shift =====================

class ShiftView(APIView):
    """ A class to create api for Shift """

    def post(self, request, formate=None, **kwargs):
        """creating Shift object"""
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of Shift objects"""
        shifts = Shift.objects.filter(madrasha__slug=madrasha_slug, is_active=True)
        serializer = ShiftListSerializer(shifts, many=True)
        return Response(serializer.data)


class ShiftDetailview(APIView):
    """ Shift detail, update and delete"""

    def get_object(self, slug):
        """get single Shift obj"""

        try:
            return Shift.objects.get(slug=slug)
        except Shift.DoesNotExist:
            return Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        shift = self.get_object(slug)
        serializer = ShiftSerializer(shift)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        shift = self.get_object(slug)
        serializer = ShiftSerializer(shift, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """ delete """
        shift = self.get_object(slug)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================== 6. Books =====================

class BooksView(APIView):
    """ A class to create api for Books """

    def post(self, request, formate=None, **kwargs):
        """creating Books object"""
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of Books objects"""
        books = Books.objects.filter(madrasha__slug=madrasha_slug)
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)


class BooksDetailview(APIView):
    """ Books detail, update and delete"""

    def get_object(self, slug):
        """get single Books obj"""

        try:
            return Books.objects.get(slug=slug)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        shift = self.get_object(slug)
        serializer = BooksSerializer(shift)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        book = self.get_object(slug)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """ delete """
        book = self.get_object(slug)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================== 7. Fees =====================


class FeesView(APIView):
    """ A class to create api for Fees """

    def post(self, request, formate=None, **kwargs):
        """creating Fees object"""
        serializer = FeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of Fees objects"""
        # madrasha_slug = kwargs.get('madrasha_slug')
        fees = Fees.objects.filter(madrasha__slug=madrasha_slug)
        serializer = FeesListSerializer(fees, many=True)
        return Response(serializer.data)


class FeesDetailview(APIView):
    """ Fees detail, update and delete"""

    def get_object(self, slug):
        """get single Fees obj"""

        try:
            return Fees.objects.get(slug=slug)
        except Fees.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        fee = self.get_object(slug)
        serializer = FeesSerializer(fee)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        fee = self.get_object(slug)
        serializer = FeesSerializer(fee, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """ delete """
        fee = self.get_object(slug)
        fee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================== 8. Session =====================

class SessionView(APIView):
    """ A class to create api for Session """

    def post(self, request, formate=None, **kwargs):
        """creating Session object"""
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, madrasha_slug, formate=None):
        """ showing a list of Session objects"""
        session = Session.objects.filter(madrasha__slug=madrasha_slug)
        serializer = SessionListSerializer(session, many=True)
        return Response(serializer.data)


class SessionDetailview(APIView):
    """ Session detail, update and delete"""

    def get_object(self, slug):
        """get single Session obj"""

        try:
            return Session.objects.get(slug=slug)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """details veiw for single obj"""
        session = self.get_object(slug)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        session = self.get_object(slug)
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """ delete """
        session = self.get_object(slug)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ================================== 9. Exam rules =====================

class ExamRulesView(APIView):
    """ A class to create api for Session """

    def post(self, request, formate=None):
        """creating Session object"""
        serializer = ExamRulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, formate=None):
        """ showing a list of Session objects"""
        exam_rules = ExamRules.objects.all()
        serializer = ExamRulesSerializer(exam_rules, many=True)
        return Response(serializer.data)


class ExamRulesDetailview(APIView):
    """ Session detail, update and delete"""

    def get_object(self, pk):
        """get single Session obj"""

        try:
            return ExamRules.objects.get(pk=pk)
        except ExamRules.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        """details veiw for single obj"""
        exam_rule = self.get_object(pk)
        serializer = ExamRulesSerializer(exam_rule)
        return Response(serializer.data)

    def put(self, request, slug, formate=None):
        """update view"""
        exam_rule = self.get_object(slug)
        serializer = ExamRulesSerializer(exam_rule, data=request.data)
        if serializer.is_valid():
            slug = serializer.validated_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, formate=None):
        """ delete """
        exam_rule = self.get_object(slug)
        exam_rule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
