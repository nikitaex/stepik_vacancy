from django.contrib import admin
from .models import Company, Vacancy, Specialty, Application


class CompanyAdmin(admin.ModelAdmin):
    pass


class VacancyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, CompanyAdmin)
admin.site.register(Specialty, CompanyAdmin)
admin.site.register(Application, CompanyAdmin)
