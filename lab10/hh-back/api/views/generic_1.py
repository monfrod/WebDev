from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status,mixins,generics

import json
from ..models import Company,Vacancy
from ..serializers import CompanySerializer,VacancySerializer,CompanySerializer2,VacancySerializer2


class CompanyList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset=Company.objects.all()
    serializer_class=CompanySerializer2
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class CompanyDetails(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer2

    def get(self,request,pk=None):
        return self.retrieve(request,pk)
    def put(self,request,pk=None):
        return self.update(request,pk)
    def delete(self,request,pk=None):
        return self.destroy(request,pk)

class VacancyList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer2
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class VacancyDetails(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer2

    def get(self,request,pk=None):
        return self.retrieve(request,pk)
    def put(self,request,pk=None):
        return self.update(request,pk)
    def delete(self,request,pk=None):
        return self.destroy(request,pk)

class VacanciesByCompanies(mixins.ListModelMixin,
                           generics.GenericAPIView):
    serializer_class=VacancySerializer2
    def get_queryset(self):
        try:
            company = Company.objects.get(id=self.kwargs['pk'])
            return Vacancy.objects.filter(Company=company)
        except Company.DoesNotExist as e:
            return Vacancy.objects.none()
    def get(self,request,pk=None):
        return self.list(request,pk)
    
class VacanciesTopTen(mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset=Vacancy.objects.order_by('-salary')[:10]
    serializer_class=VacancySerializer2
    def get(self,request):
        return self.list(self,request)    



