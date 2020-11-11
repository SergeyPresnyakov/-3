"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких
чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу"""

sum_numbers_str = 0


def summa(*args):
    global numbers_number_new
    global sum_numbers_str
    for i in range(len(numbers_number_new)):
        numbers_number_new[i] = int(numbers_number_new[i])

    numbers_number_new = sum(numbers_number_new)
    sum_numbers_str = sum_numbers_str + numbers_number_new

    (print(f"Сумма введенных чисел = {sum_numbers_str}"))


while True:
    numbers_str_new = str(input("Введите строку чисел, разделенных пробелом: "))

    numbers_number_new = numbers_str_new.split()

    if numbers_str_new == "b":
        break

    if numbers_number_new[-1] == "b":
        numbers_number_new = numbers_number_new[: -1]
        summa()
        break

    else:
        summa()
        continue
