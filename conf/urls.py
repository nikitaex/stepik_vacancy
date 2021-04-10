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
from vacancies.views import custom_handler404, custom_handler500, SendVacancyView, MyCompanyCreateOfferView, \
    MyCompanyCreateView, MyCompanyEditView, MyVacanciesList, MyVacancyEditView, MyVacancyCreateView, MyLogoutView
from vacancies.views import MainView, VacanciesView, SpecializationByVacanciesView, CompanyCardView, VacancyView, \
    MySignupView, MyLoginView

handler404 = custom_handler404
handler500 = custom_handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:specialization>/', SpecializationByVacanciesView.as_view()),
    path('companies/<int:company_id>', CompanyCardView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', MyLogoutView.as_view(), name="logout"),
    path('register/', MySignupView.as_view(), name="register"),
    path('vacancies/<int:vacancy_id>/send', SendVacancyView.as_view(), name="send"),
    path('mycompany/letsstart', MyCompanyCreateOfferView.as_view(), name="company_create_offer"),
    path('mycompany/create', MyCompanyCreateView.as_view(), name="company_create"),
    path('mycompany/', MyCompanyEditView.as_view(), name="company_edit"),
    path('mycompany/vacancies', MyVacanciesList.as_view(), name="vacancies_list"),
    path('mycompany/vacancies/create/', MyVacancyCreateView.as_view(), name="vacancy_create"),
    path('mycompany/vacancies/<int:pk>', MyVacancyEditView.as_view(), name="vacancy_edit"),
]
