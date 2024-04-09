from django.shortcuts import render

from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
from django.http import JsonResponse

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailID(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        company_id = self.kwargs.get('id')
        try:
            company = self.queryset.get(id=company_id)
            serializer = self.get_serializer(company)
            return JsonResponse(serializer.data)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company does not exist'}, status=404)

class VacancyListByCompany(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)

class VacancyList(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailID(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get(self, request, *args, **kwargs):
        vacancy_id = self.kwargs.get('id')
        try:
            vacancy = self.queryset.get(id=vacancy_id)
            serializer = self.get_serializer(vacancy)
            return JsonResponse(serializer.data)
        except Vacancy.DoesNotExist:
            return JsonResponse({'error': 'Vacancy does not exist'}, status=404)

class TopTenVacancies(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.order_by('-salary')[:10]

