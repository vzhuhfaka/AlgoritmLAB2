import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab1.utils import read_data, write_data

def task8(N, applications):
    applications.sort(key=lambda x: x[1])  # сортируем по времени окончания

    selected = []
    last_end_time = 0

    for start, end in applications:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end

    return len(selected)


def main():
    # Входные данные
    PATH_INPUT = 'lab1/task8/txtf/input.txt'
    PATH_OUTPUT = 'lab1/task8/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    N_ = int(data[0])
    applications_ = [[int(i[0]), int(i[1])] for i in[j.split() for j in data[1:]]]  # ['a b'] -> [a, b]

    print('Лабораторная 1 Задача 8')
    print(f'Входные данные: {data}')
    answer = task8(N_, applications_)
    print(f'Вывод: {answer}')
    write_data(PATH_OUTPUT, str(answer))
    print('-'*30)


if __name__ == '__main__':
    main()