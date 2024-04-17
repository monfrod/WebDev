from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Company,Vacancy
from ..serializers import CompanySerializer,VacancySerializer,CompanySerializer2,VacancySerializer2

# Create your views here.

@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies= Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def companiesById(request,pk=None):

    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return HttpResponse(status=404)
    

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer2(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacancies= Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def vacanciesById(request,pk=None):

    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist:
        return HttpResponse(status=404)
    

    if request.method == 'GET':
        serializer = VacancySerializer2(vacancy)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = VacancySerializer2(vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vacancy.delete()
        return HttpResponse(status=204)
    
def vacanciesByCompanies(request,pk=None):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    
    vacancies=Vacancy.objects.filter(Company=company)

    serializer = VacancySerializer2(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

def vacanciesTopTen(request):
    vacancies=Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer2(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

