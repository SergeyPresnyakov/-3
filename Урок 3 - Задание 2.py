"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""
"""Функция с именованными параметрами"""


def user_info(name, surname, year_birth, city, email, tel):
    print(f"{name} {surname} {year_birth} {city} {email} {tel}")


user_info(surname="Пресняков", name="Сергей", year_birth="1981", city="Оренбург",
          email="sergey@yandex.ru", tel="89198547857")

"""Функция с конструкцией **kwargs"""


def user_info_kwargs(**kwargs):
    return (" ".join(kwargs.values()))


print(user_info_kwargs(surname="Пресняков", name="Сергей", year_birth="1981", city="Оренбург",
                       email="sergey@yandex.ru", tel="89198547857"))
