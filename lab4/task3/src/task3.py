import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab4.utils import read_data, print_data


def polynom_hash_func(string, p=31, m=10 ** 9 + 7):
    """Полиномиальная хеш-функция для строки"""
    hash_value = 0
    p_pow = 1

    for char in string:
        # Добавляем ASCII код символа, умноженный на текущую степень p
        hash_value = (hash_value + ord(char) * p_pow) % m
        # Увеличиваем степень p для следующего символа
        p_pow = (p_pow * p) % m

    return hash_value


def task1(data, target):
    """Использует алгоритм Рабина-Карпа для поиска заданного шаблона"""
    indexes = []

    target_hash = polynom_hash_func(target)
    target_len = len(target)
    for i in range(len(data)):
        cur_word = data[i:(i+target_len)]
        cur_word_hash = polynom_hash_func(cur_word)
        if target_hash == cur_word_hash:  # проверям совпадение хешей
            # Проверяем посимвольно, чтобы избежать коллизий
            if target == cur_word:
                indexes.append(i+1)

    return indexes


def main() -> None:
    """Функция собирающая и обрабатывающая все данные"""

    # Входные данные
    PATH_INPUT = 'lab4/task3/txtf/input.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    # Обработка
    answer = task1(data=data[1],
                    target=data[0])

    # Данные о задаче
    print_data(number_lab=4, number_task=3, input_data=data, output_data=(len(answer), answer))
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()