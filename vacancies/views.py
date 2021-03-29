from django.http import HttpResponseServerError, Http404
from django.shortcuts import render
from django.views import View
from vacancies.models import Vacancy, Specialty, Company
from django.db.models import Count


class MainView(View):
    def get(self, request):
        return render(
            request, 'pages/index.html', context={
                'speciality_all': Specialty.objects.all(),
                'speciality_count': Specialty.objects.annotate(count=Count('vacancies')),
                'companies': Company.objects.all(),
                'vacancies_count': Company.objects.annotate(count_vacancy=Count('vacancies')),
            },
        )


class VacanciesView(View):
    def get(self, request):
        return render(request, 'pages/vacancies.html', context={
                'vacancies': Vacancy.objects.all(),
                'vacancies_count': Vacancy.objects.all().count(),
            },
        )


class SpecializationByVacanciesView(View):
    def get(self, request, specialization):
        try:
            specialization = Specialty.objects.get(code=specialization)
        except KeyError:
            raise Http404
        return render(request, 'pages/vacancies_by_specialization.html', context={
                'vacancies': Vacancy.objects.filter(specialty__code=specialization.code),
                'vacancies_count': Vacancy.objects.filter(specialty__code=specialization.code).count(),
                'specialization': specialization,
            },
        )


class CompanyCardView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except KeyError:
            raise Http404
        return render(request, 'pages/company.html', context={
                'company': Company.objects.get(id=company.id),
                'vacancies_count': Vacancy.objects.filter(company__id=company.id).count(),
                'vacancies': Vacancy.objects.filter(company__id=company.id),
            },
        )


class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Company.objects.get(id=vacancy_id)
        except KeyError:
            raise Http404
        return render(request, 'pages/vacancy.html', context={
                'vacancy': Vacancy.objects.get(id=vacancy.id),
            },
        )


def custom_handler404(request, exception):
    return Http404('Ой, что то сломалось... Простите извините!(404)')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
