from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)


class Vacancy(models.Model):
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    salary_from = models.PositiveIntegerField()
    salary_to = models.PositiveIntegerField()
    salary_currency = models.CharField(max_length=10)
