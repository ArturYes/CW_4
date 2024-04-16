import json
import os
from abc import ABC, abstractmethod

from config import PATH_JSON_ALL_VACANCY, PATH_FOLDER


class BaseSaver(ABC):
    """Абстрактный класс сохранения"""

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """
        Абстрактный метод добавления вакансии
        :param vacancy: вакансия
        :return: None
        """
        pass

    @abstractmethod
    def get_filter_vacancy(self, key, value) -> list[dict] | str:
        """
        Абстрактный метод получения вакансий по критериям
        :param key: поле поиска
        :param value: значение для поиска
        :return: список вакансий
        """

    @abstractmethod
    def del_vacancy(self, vacancy) -> None:
        """
        Абстрактный метод удаления вакансии
        :param vacancy: вакансия
        :return: None
        """
        pass


class JsonSaver(BaseSaver):
    """Класс сохранения вакансий в json файл"""

    def __init__(self):
        self.file_path = PATH_JSON_ALL_VACANCY

    def add_vacancy(self, vacancy: dict) -> None:
        """
        Метод добавления вакансии в json файл
        :param vacancy: вакансия для добавления
        :return: None
        """
        if not os.path.exists(PATH_FOLDER):
            os.mkdir(PATH_FOLDER)
        with open(self.file_path, "a", encoding='UTF-8') as f:
            if os.stat(self.file_path).st_size == 0:
                json.dump([vacancy], f, indent=2, ensure_ascii=False)
            else:
                with open(self.file_path, encoding='UTF-8') as file:
                    data_vacancy = json.load(file)
                data_vacancy.append(vacancy)
                with open(self.file_path, "w", encoding='UTF-8') as outfile:
                    json.dump(data_vacancy, outfile, indent=2, ensure_ascii=False)

    def get_filter_vacancy(self, key: str, value: str) -> list[dict] | str:
        """
        Метод получения списка вакансий из json файла
        :param key: поле поиска
        :param value: значение для поиска
        :return: список словарей или строку
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, encoding='UTF-8') as file:
                data_vacancy = json.load(file)
            vacancy_filter = []
            for vacancy in data_vacancy:
                if value in vacancy[key]:
                    vacancy_filter.append(vacancy)
            if vacancy_filter:
                return vacancy_filter
            else:
                return "Вакансии по заданным критериям не найдены"
        else:
            return "Несуществующий путь."

    def del_vacancy(self, vacancy) -> None:
        """
        Метод удаления вакансии из json файла
        :param vacancy: вакансия для удаления
        :return: None
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, encoding='UTF-8') as file:
                data_vacancy = json.load(file)
            if vacancy in data_vacancy:
                for item in data_vacancy:
                    if item == vacancy:
                        index = data_vacancy.index(item)
                        del data_vacancy[index]
                        print("Вакансия найдена. Удаляем...")
                        break
                with open(self.file_path, "w", encoding='UTF-8') as outfile:
                    json.dump(data_vacancy, outfile, indent=2, ensure_ascii=False)
            else:
                print("Такой вакансии нет")
        else:
            print("Несуществующий путь.")
