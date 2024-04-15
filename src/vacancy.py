class Vacancy:
    def __init__(self, **kwargs: dict) -> None:
        """Инициализация параметров вакансии"""
        self.name = kwargs['name']
        self.salary = kwargs['salary']
        self.experience = kwargs['experience']['name']
        requirement = kwargs.get('snippet').get('requirement')
        responsibility = kwargs.get('snippet').get('responsibility')
        self.description = f"{requirement if requirement else ''}{' ' + responsibility if responsibility else ''}"
        self.area = kwargs.get('area').get('name')
        self.employer = kwargs.get('employer').get('name')
        self.url_vacancy = kwargs.get('alternate_url')

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