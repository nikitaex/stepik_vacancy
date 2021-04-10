from django.db import models
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=200)
    employee_count = models.IntegerField()
    owner = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,
                                 related_name="company")

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
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = models.CharField(max_length=13)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(get_user_model(), default="", on_delete=models.CASCADE, related_name="applications")

    def __str__(self):
        return self.user
