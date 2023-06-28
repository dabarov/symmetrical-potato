import requests
from celery import shared_task

from vacancies.models import Company, Vacancy

COMPANY_NAME_KOLESA_GROUP = "Kolesa Group"
COMPANY_VACANCY_URL_KOLESA = "https://kolesa.group/api/career/vacancy"
DEV_VACANCIES_KOLESA_GROUP = "dev"


@shared_task
def kolesa_group_dev_vacancies():
    kolesa_group_company = Company.objects.get(name=COMPANY_NAME_KOLESA_GROUP)
    response = requests.get(COMPANY_VACANCY_URL_KOLESA)
    data = response.json()
    dev_vacancies = data.get("dev").get("vacancies")
    for vacancy in dev_vacancies:
        vacancy_salary = vacancy.get("salary")
        Vacancy.objects.create(
            company=kolesa_group_company,
            position=vacancy.get("position"),
            location=vacancy.get("area"),
            salary_from=vacancy_salary.get("from") or 0,
            salary_to=vacancy_salary.get("to") or 0,
            salary_currency=vacancy_salary.get("currency") or "",
        )
