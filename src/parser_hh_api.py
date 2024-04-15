from abc import ABC, abstractmethod

import requests


class JobVacancyAPI(ABC):
    """Абстрактный класс пря поиска вакансий через API"""

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """
        Абстрактный метод получения вакансий
        :param keyword: ключевое слово для поиска
        :return:
        """
        pass


class HH(JobVacancyAPI):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'text': '',
            'only_with_salary': True,
            'area': 113,
            'page': 0,
            'per_page': 100
        }
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод получения вакансий от HH
        :param keyword: ключевое слово
        :return: список словарей вакансий
        """
        self.params['text'] = keyword

        while True:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                resp = response.json()
                page = resp['page']
                pages = resp['pages']
                vacancies = resp['items']
                self.vacancies.extend(vacancies)
                print(f'Загружены вакансии. Страница {page + 1} из {pages}')
                if page == pages - 1:
                    break
                self.params['page'] += 1
        return self.vacancies
