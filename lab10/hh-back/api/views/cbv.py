from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

import json
from ..models import Company,Vacancy
from ..serializers import CompanySerializer,VacancySerializer,CompanySerializer2,VacancySerializer2


class CompanyListAPIView(APIView):
    def get(self,request):
        companies= Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CompanyDetailsAPIView(APIView):
    def getCompany(self,pk=None):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist as err:
            return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk=None):
        company=self.getCompany(pk)
        serializer = CompanySerializer2(company)
        return Response(serializer.data)
    def put(self,request,pk=None):
        company=self.getCompany(pk)
        serializer = CompanySerializer2(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        company=self.getCompany(pk)
        company.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)

class VacancyListAPIView(APIView):
    def get(self,request):        
        vacancies= Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):   
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class VacancyDetailsAPIView(APIView):
    def getVacancy(self,pk=None):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist as err:
            return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk=None):
        vacancy=self.getVacancy(pk)
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)
    def put(self,request,pk=None):
        vacancy=self.getVacancy(pk)
        serializer = VacancySerializer2(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        vacancy=self.getVacancy(pk)
        vacancy.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)

class VacanciesByCompaniesAPIView(APIView):
    def get(self,request,pk=None):
        try:
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        
        vacancies=Vacancy.objects.filter(Company=company)

        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class VacanciesTopTenAPIView(APIView):
    def get(self,request):
        vacancies=Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    






