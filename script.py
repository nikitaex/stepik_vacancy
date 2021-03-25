import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

from data import jobs, companies, specialties
from vacancies.models import Vacancy, Specialty, Company


if __name__ == '__main__':

    for company in companies:
        Company.objects.create(
            name=company["title"],
            location=company["location"],
            description=company["description"],
            employee_count=company["employee_count"]
        )

    for specialty in specialties:
        Specialty.objects.create(
            code=specialty["code"],
            title=specialty["title"]
        )

    for job in jobs:
        Vacancy.objects.create(
            title=job["title"],
            specialty=Specialty.objects.get(code=job["specialty"]),
            company=Company.objects.get(id=job["company"]),
            skills=job["skills"],
            description=job["description"],
            salary_min=job["salary_from"],
            salary_max=job["salary_to"],
            published_at=job["posted"]
        )
