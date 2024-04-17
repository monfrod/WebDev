from django.db import models

# Create your models here.

class Company(models.Model):
    name =        models.CharField(max_length=255)
    description = models.TextField() 
    city =        models.CharField(max_length=255)
    address =     models.TextField()

    def __str__(self) -> str:
        return f"name:{self.name},description:{self.description},city:{self.city},address:{self.address}"
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"



class Vacancy(models.Model):
    name =        models.CharField(max_length=255)
    description = models.TextField() 
    salary =      models.FloatField()
    Company =     models.ForeignKey(Company,on_delete=models.CASCADE,related_name="vacancy")

    def __str__(self) -> str:
        return f"name:{self.name},description:{self.description},salary:{self.salary},company:{self.Company.__str__()}"
    

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"