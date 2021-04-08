from django import forms

from vacancies.models import Company, Vacancy


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count', 'owner')


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')
