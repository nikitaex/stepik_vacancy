from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from vacancies.forms import CompanyForm, VacancyForm
from vacancies.models import Vacancy, Specialty, Company
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, ListView


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'pages/register.html'


class MyLoginView(LoginView):
    template_name = 'pages/login.html'


class MyLogoutView(LogoutView):
    pass


class BaseCompanyView:
    model = Company
    form_class = CompanyForm


class BaseVacancyView:
    model = Vacancy
    form_class = VacancyForm


class SendVacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        return render(request, 'pages/send.html', context={
            'vacancy': Vacancy.objects.get(id=vacancy.id)})


class MyCompanyCreateOfferView(View):
    def get(self, request):
        return render(request, 'pages/company-create.html')


class MyCompanyCreateView(BaseCompanyView, CreateView):
    template_name = 'pages/company-edit.html'


class MyCompanyEditView(BaseCompanyView, UpdateView):
    template_name = 'pages/company-edit.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)


class MyVacanciesList(BaseVacancyView, ListView):
    context_object_name = 'vacancies'
    template_name = 'pages/vacancy-list.html'


class MyVacancyCreateView(BaseVacancyView, CreateView):
    template_name = 'pages/vacancy-edit.html'

    def get_success_url(self):
        return reverse('vacancy_edit', kwargs={'pk': self.object.pk})


class MyVacancyEditView(BaseVacancyView, UpdateView):
    template_name = 'pages/vacancy-edit.html'

    def get_success_url(self):
        return reverse('vacancy_edit', kwargs={'pk': self.object.pk})


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
