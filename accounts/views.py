'''
1.dependent drop down for address
2. individual address
3. MadrashaView
'''

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from .models import *
from .serializers import AddressSerializer, MadrashaSerializer

# Create your views here.

#  ====================================== 1.dependent drop down for address ==========================


class DistrictList(APIView):
    def post(self, request):
        division = request.data['division']
        district = {}
        if division:
            districts = Division.objects.get(id=division).districts.all()
            district = {d.name:d.id for d in districts}
        return JsonResponse(data=district, safe=False)


class ThanaList(APIView):
    def post(self, request):
        district = request.data['district']
        thana = {}
        if district:
            thanas = District.objects.get(id=district).thanas.all()
            thana = {d.name:d.id for d in thanas}
        return JsonResponse(data=thana, safe=False)


class PostOfficeList(APIView):
    def post(self, request):
        district = request.data['district']
        post_office = {}
        if district:
            post_offices = District.objects.get(id=district).postoffices.all()
            post_office = {d.name:d.id for d in post_offices}
        return JsonResponse(data=post_office, safe=False)


class PostCodeList(APIView):
    def post(self, request):
        post_office = request.data['post_office']  # here post_code is the var from form
        post_code = {}
        if post_office:
            post_codes = PostOffice.objects.get(id=post_office).postcodess.all()
            post_code = {d.name:d.id for d in post_codes}
        return JsonResponse(data=post_code, safe=False)


# ==================== 2. individual address ============


class AddressDetail(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)


# ===================== 3. MadrashaView ============
#
# class MadrashaView(ListCreateAPIView):
#     queryset = Madrasha.objects.all()
#     serializer_class = MadrashaSerializer
#
#
# class MadrashaDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = MadrashaSerializer
#     lookup_url_kwarg = 'slug'
#     queryset = Madrasha.objects.all()



