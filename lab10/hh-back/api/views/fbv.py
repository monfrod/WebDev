from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

import json
from ..models import Company,Vacancy
from ..serializers import CompanySerializer,VacancySerializer,CompanySerializer2,VacancySerializer2


@api_view(["GET","POST"])
def companies(request):
    if request.method == 'GET':
        companies= Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def companiesById(request,pk=None):

    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer2(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET","POST"])
def vacancies(request):
    if request.method == 'GET':
        vacancies= Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def vacanciesById(request,pk=None):

    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer2(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)
@api_view(["GET"])
def vacanciesByCompanies(request,pk=None):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    
    vacancies=Vacancy.objects.filter(Company=company)

    serializer = VacancySerializer2(vacancies, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(["GET"])
def vacanciesTopTen(request):
    vacancies=Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer2(vacancies, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

