from django.contrib import admin
from .models import Company,Vacancy
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','name','city','address')
    search_fields=('id','name','city','address')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display=('id','name','salary')
    search_fields=('id','name','salary')