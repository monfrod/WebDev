from rest_framework import serializers
from .models import Company,Vacancy


class CompanySerializer(serializers.Serializer):
    id =          serializers.IntegerField()
    name =        serializers.CharField()
    description = serializers.CharField()
    city =        serializers.CharField()
    address =     serializers.CharField()

    def create(self, validated_data):

        return Company.objects.create(**validated_data)

    def update(self, instance:Company, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    class Meta:
        model = Company
        fields = "__all__"



class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"



class VacancySerializer(serializers.Serializer):
    id =          serializers.IntegerField()
    name =        serializers.CharField()
    description = serializers.CharField()
    salary =      serializers.FloatField()
    Company =     CompanySerializer()


    def create(self, validated_data):

        company_data = validated_data.pop('Company')
        company_id = company_data.get('id')
        company_instance = Company.objects.get(id=company_id)

        return Vacancy.objects.create(Company=company_instance, **validated_data)

    def update(self, instance:Vacancy, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.description = validated_data.get('description', instance.description)

    
        company_data = validated_data.get('Company')
        company_id = company_data.get('id')
        if company_id:
            try:
                company_instance = Company.objects.get(id=company_id)
                instance.Company = company_instance
            except Company.DoesNotExist:
                raise serializers.ValidationError("Company with provided ID does not exist")

        instance.save()
        return instance
    
    class Meta:
        model = Vacancy
        fields = "__all__"

    
class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"