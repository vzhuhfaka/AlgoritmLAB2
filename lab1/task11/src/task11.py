import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab1.utils import read_data, write_data

def task11(W, weights):
    n = len(weights)
    dp = [0] * (W + 1)

    # Заполняем массив dp
    for i in range(n):
        for j in range(W, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + weights[i])

    return dp[W]


def main():
    # Входные данные
    PATH_INPUT = 'lab1/task11/txtf/input.txt'
    PATH_OUTPUT = 'lab1/task11/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    W_backpack_ = int(data[0].split()[0])
    w_ = [int(i) for i in data[1].split()]

    print('Лабораторная 1 Задача 11')
    print(f'Входные данные: {data}')
    answer = task11(W_backpack_, w_)
    print(f'Вывод: {answer}')
    write_data(PATH_OUTPUT, str(answer))
    print('-'*30)


if __name__ == '__main__':
    main()