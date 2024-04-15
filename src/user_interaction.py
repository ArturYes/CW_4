from src.parser_hh_api import HH
from src.vacancy import Vacancy
from src.vacancy_saver import JsonSaver


def start_app():
    hh_api = HH()
    user_query = input("\nВведите поисковый запрос(например: Python): ")
    list_vacancy = hh_api.load_vacancies(user_query)

    vacancies_all_obj = []
    for vacancy in list_vacancy:
        vacancies_all_obj.append(Vacancy(**vacancy))

    total = len(vacancies_all_obj)
    save = JsonSaver()

    for num, vacancy_obj in enumerate(vacancies_all_obj, 1):
        save.add_vacancy(vacancy_obj.__dict__)
        if num % 100 == 0:
            print(f"Сохранено вакансий {num} из {total}")
