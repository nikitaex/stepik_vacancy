from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from vacancies.models import Vacancy, Specialty, Company
from django.db.models import Count


class MainView(View):
    def get(self, request):
        return render(
            request, 'pages/index.html', context={
                'speciality_backend': Specialty.objects.filter(code="backend"),
                'speciality_backend_count': Specialty.objects.filter(code="backend").count(),
                'companies': Company.objects.all(),
                'vacancies_count': Company.objects.annotate(count_vacancy=Count('vacancies'))
            }
        )


class VacanciesView(View):
    def get(self, request):
        return render(request, 'pages/vacancies.html', context={
                'vacancies': Vacancy.objects.all(),
                'vacancies_count': Vacancy.objects.all().count(),
            }
        )


class SpecializationByVacanciesView(View):
    def get(self, request, specialization):
        specialization = Specialty.objects.get(code=specialization)
        return render(request, 'pages/vacancies_by_specialization.html', context={
                'vacancies': Vacancy.objects.filter(specialty__code=specialization),
                'vacancies_count': Vacancy.objects.filter(specialty__code=specialization).count(),
                'specialization': specialization,
            }
        )


class company_card_view(View):
    def get(self, request):
        return render(request, 'pages/company.html')


class vacancy_view(View):
    def get(self, request):
        return render(request, 'pages/vacancy.html')
