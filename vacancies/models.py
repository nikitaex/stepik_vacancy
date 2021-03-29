from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=200)
    employee_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}{self.location}'


class Specialty(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return self.title
