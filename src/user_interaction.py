from src.parser_hh_api import HH
from src.vacancy import Vacancy


def start_app():

    hh_api = HH()
    user_query = input("\nВведите поисковый запрос(например: Python): ")
    list_vacancy = hh_api.load_vacancies(user_query)

    vacancies_all_obj = []
    for vacancy in list_vacancy:
        vacancies_all_obj.append(Vacancy(**vacancy))

    for num, i in enumerate(vacancies_all_obj, 1):
        print(f"{num}: {i}")