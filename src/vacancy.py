class Vacancy:
    def __init__(self, **kwargs: dict) -> None:
        """Инициализация параметров вакансии"""
        self.name = kwargs['name']
        self.salary = kwargs['salary']

        if isinstance(kwargs['experience'], dict):
            self.experience = kwargs['experience']['name']
        elif isinstance(kwargs['experience'], str):
            self.experience = kwargs['experience']

        if kwargs.get('description'):
            self.description = kwargs['description']
        elif kwargs.get('snippet'):
            requirement = kwargs.get('snippet').get('requirement')
            responsibility = kwargs.get('snippet').get('responsibility')
            description = f"{requirement if requirement else ''}{' ' + responsibility if responsibility else ''}"
            self.description = description

        if isinstance(kwargs['area'], dict):
            self.area = kwargs.get('area').get('name')
        else:
            self.area = kwargs['area']

        if isinstance(kwargs['employer'], dict):
            self.employer = kwargs.get('employer').get('name')
        else:
            self.employer = kwargs['employer']

        if kwargs.get('alternate_url'):
            self.url_vacancy = kwargs['alternate_url']
        else:
            self.url_vacancy = kwargs['url_vacancy']

    @property
    def from_salary(self):
        """Геттер возвращающий значение зарплаты от"""
        if self.salary is None:
            from_salary = 0
        else:
            from_salary = self.salary.get('from')
        return from_salary

    @property
    def to_salary(self):
        """Геттер возвращающий значение зарплаты до"""
        if self.salary is None:
            to_salary = 0
        else:
            to_salary = self.salary.get('to')
        return to_salary

    @property
    def value(self) -> int:
        """Геттер берущий значение для сравнения при сортировке"""
        if self.from_salary and self.to_salary:
            value = (self.from_salary + self.to_salary) // 2
        elif self.from_salary and not self.to_salary:
            value = self.from_salary
        elif not self.from_salary and self.to_salary:
            value = self.to_salary
        return value

    @property
    def check_salary(self):
        """Геттер возвращающий строку зарплаты """
        if self.from_salary and not self.to_salary:
            return f"Зарплатная вилка от {self.from_salary}"
        elif not self.from_salary and self.to_salary:
            return f"Зарплатная вилка до {self.to_salary}"
        elif self.from_salary and self.to_salary:
            return f"Зарплатная вилка от {self.from_salary} до {self.to_salary}"
        else:
            return "Зарплата не указана"

    def __repr__(self) -> str:
        """Вывод вакансии для разработчика"""
        return (f"{self.__class__.__name__}("
                f"{self.name}, {self.salary}, "
                f"{self.experience}, {self.description}, "
                f"{self.area}, {self.employer}, {self.url_vacancy})")

    def __str__(self) -> str:
        """Вывод вакансии для пользователя"""
        return (f"Название вакансии - {self.name}\n"
                f"{self.check_salary}\n"
                f"Требуемый опыт {self.experience}\n"
                f"Наименование организации - {self.employer}\n"
                f"Город расположения - {self.area}\n"
                f"Ссылка на вакансию - {self.url_vacancy}\n")

    def __gt__(self, other) -> bool:
        """Метод сравнения вакансий"""
        return self.value > other.value

    @staticmethod
    def filter_vacancies(list_vacancy: list, filters: list) -> list:
        """
        Фильтрации списка по ключевым словам
        :param list_vacancy: список вакансий
        :param filters: список ключевых слов
        :return: отфильтрованный список вакансий
        """
        if not filters:
            return list_vacancy

        filtered_vacancies = []
        for item in list_vacancy:
            description = item.description.lower()
            if all(word in description for word in filters):
                filtered_vacancies.append(item)
        return filtered_vacancies

    @staticmethod
    def sort_vacancies(list_vacancy: list) -> list:
        """
        Сортировка вакансий по зарплате
        :param list_vacancy: Список вакансий
        :return: отсортированный список
        """
        return sorted(list_vacancy, reverse=True)

    @staticmethod
    def get_top_vacancies(list_vacancy: list, num: str) -> list:
        """
        Получение топ вакансий
        :param list_vacancy: список вакансий
        :param num: количество вакансий для возврата
        :return: список топ вакансий
        """
        if num == "":
            num = len(list_vacancy)
        elif num.isdigit():
            num = int(num)
        if 0 < len(list_vacancy) <= num:
            return list_vacancy
        else:
            return list_vacancy[0:num]

    @staticmethod
    def print_list_vacancy(list_vacancy: list) -> None:
        """
        Вывода вакансий
        :param list_vacancy: список вакансий
        """
        for index, item in enumerate(list_vacancy, 1):
            print(f"Вакансия №{index}:\n"
                  f"{item}")

    @staticmethod
    def filter_name(list_vacancy: list, user_answer: str) -> None:
        """
        Сортировки по названию вакансии
        :param list_vacancy: список вакансий
        :param user_answer: слово для фильтрации
        :return: None
        """
        index = 0
        for item in list_vacancy:
            if user_answer in item.name.lower():
                index += 1
                print(f"Вакансия №{index}:\n"
                      f"{item}")
        if index == 0:
            print("\nПодходящих вакансий не найдено. Попробуйте изменить запрос")
        else:
            print(f"Всего вакансий получено: {index}")

    @staticmethod
    def filter_city(list_vacancy: list, user_answer: str) -> None:
        """
        Сортировка по городу
        :param list_vacancy: список вакансий
        :param user_answer: город для фильтрации
        :return:
        """
        index = 0
        for item in list_vacancy:
            if user_answer in item.area.lower():
                index += 1
                print(f"Вакансия №{index}:\n"
                      f"{item}")
        if index == 0:
            print("\nПодходящих вакансий не найдено. Попробуйте изменить запрос")
        else:
            print(f"Всего вакансий получено: {index}")

    @staticmethod
    def filter_company(list_vacancy: list, user_answer: str) -> None:
        """
        Сортировка по названию компании
        :param list_vacancy: список вакансий
        :param user_answer: название компании
        :return:
        """
        index = 0
        for item in list_vacancy:
            if user_answer == item.employer.lower():
                index += 1
                print(f"Вакансия №{index}:\n"
                      f"{item}")
        if index == 0:
            print("\nПодходящих вакансий не найдено. Попробуйте изменить запрос")
        else:
            print(f"Всего вакансий получено: {index}")

    @staticmethod
    def filter_salary(list_vacancy: list, user_from: int, user_to: int) -> None:
        """
        Сортировка вакансий по зарплате
        :param list_vacancy: список вакансий
        :param user_from: нижнее значение зарплаты
        :param user_to: верхнее значение зарплаты
        :return:
        """
        index = 0
        for item in list_vacancy:
            if item.salary:
                if item.from_salary and item.to_salary:
                    if item.from_salary == user_from and item.to_salary == user_to:
                        index += 1
                        print(f"Вакансия №{index}:\n"
                              f"{item}")
                elif item.from_salary and not item.to_salary:
                    if item.from_salary in range(user_from, user_to + 1):
                        index += 1
                        print(f"Вакансия №{index}:\n"
                              f"{item}")
                elif not item.from_salary and item.to_salary:
                    if item.to_salary in range(user_from, user_to + 1):
                        index += 1
                        print(f"Вакансия №{index}:\n"
                              f"{item}")
        if index == 0:
            print("\nПодходящих вакансий не найдено. Попробуйте изменить запрос")
        else:
            print(f"Всего вакансий получено: {index}")
