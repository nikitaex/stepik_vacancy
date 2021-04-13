from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from vacancies.models import Company, Vacancy, Application


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

        self.helper.form_class = 'form-group'
        self.helper.label_class = 'form-group'
        self.helper.field_class = 'form-group'


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-group'
        self.helper.label_class = 'form-group'
        self.helper.field_class = 'form-group'
