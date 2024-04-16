## Проект: взаимодействие с API HeadHunter

### Технологии:

- requests 2.31.0
- json
- os
- ООП подход

### Инструкция для запуска проекта:

1. Клонировать проект
2. Создать и активировать виртуального окружения
3. Установить зависимости
4. Запустить проект

#### Клонирование проекта:

- git clone https://github.com/ArturYes/CW_4.git

#### Настройка виртуального окружение и установка зависимостей:

- [Инструкция по установке](https://sky.pro/media/kak-sozdat-virtualnoe-okruzhenie-python/)

#### Запуск проекта:

- Для старта проекта запустите файл main.py и выбираем действия запрашиваемые программой.

### Описание проекта:

- При запуске программы пользователю предлагается выбор получить вакансии от API или
  работать с уже существующим json файлом вакансий.
- При выборе получения от API у пользователя запрашивается ключевой запрос для поиска.
  Далее идет получение вакансий и сохранение их json файл,
  затем пользователь может указать ключевые слова для фильтрации (можно не указывать) и
  далее количество вакансий для вывода. После этого вывода вакансий пользователю предлагается
  сохранить этот список или отказаться.
- При выборе работы с существующим json файлом пользователю предлагается сделать выбор
  по каким параметрам вывести вакансии из json файла.
  Доступные параметры: по ключевому слову, по городу, по названию компании, по зарплате.
