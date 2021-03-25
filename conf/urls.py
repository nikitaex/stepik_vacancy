"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vacancies.views import custom_handler404, custom_handler500
from vacancies.views import MainView, VacanciesView, SpecializationByVacanciesView, CompanyCardView, VacancyView

handler404 = custom_handler404
handler500 = custom_handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:specialization>/', SpecializationByVacanciesView.as_view()),
    path('companies/<int:company_id>', CompanyCardView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),

]
