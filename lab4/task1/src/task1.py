import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab3.utils import read_data, print_data


def task1(data, target):
    indexes = []
    t_len = len(target)
    for i in range(len(data)-t_len+1):
        if data[i:(i+t_len)] == target:
            indexes.append(i+1)
    return indexes


def main() -> None:
    """
    Функция собирающая и обрабатывающая все данные
    """
    # Входные данные
    PATH_INPUT = 'lab4/task1/txtf/input.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    # Обработка
    answer = task1(data=data[1],
          target=data[0])

    # Данные о задаче
    print_data(number_lab=4, number_task=1, input_data=data, output_data=(len(answer), answer))
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()