import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab1.utils import read_data, write_data

def MinAndMax(i, j, m, M, op):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        if op[k] == '+':
            a = M[i][k] + M[k + 1][j]
            b = M[i][k] + m[k + 1][j]
            c = m[i][k] + M[k + 1][j]
            d = m[i][k] + m[k + 1][j]
            minimum = min(minimum, a, b, c, d)
            maximum = max(maximum, a, b, c, d)
        elif op[k] == '-':
            a = M[i][k] - M[k + 1][j]
            b = M[i][k] - m[k + 1][j]
            c = m[i][k] - M[k + 1][j]
            d = m[i][k] - m[k + 1][j]
            minimum = min(minimum, a, b, c, d)
            maximum = max(maximum, a, b, c, d)
        elif op[k] == '*':
            a = M[i][k] * M[k + 1][j]
            b = M[i][k] * m[k + 1][j]
            c = m[i][k] * M[k + 1][j]
            d = m[i][k] * m[k + 1][j]
            minimum = min(minimum, a, b, c, d)
            maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def maxValue(d, op):
    n = len(d)
    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, op)
    return M[0][n-1]


def format_data(data):
    '''
    Форматирует данные к виду
    'a+b-c*d' -> op=['+', '-', '*'], d=[a, b, c d]

    :param data: str
    :return: (list, list)
    '''
    t = ''
    op = []
    d = []
    for i in data:
        if i in '1234567890':
            t += i
        else:
            op.append(i)
            if t:
                d.append(int(t))
                t = ''
    if t:
        d.append(int(t))
    return d, op


def task14():
    # Входные данные
    PATH_INPUT = 'lab1/task14/txtf/input.txt'
    PATH_OUTPUT = 'lab1/task14/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    d_, op_ = format_data(data[0])

    print('Лабораторная 1 Задача 14')
    print(f'Входные данные: {data}')
    answer = maxValue(d_, op_)
    print(f'Вывод: {answer}')
    write_data(PATH_OUTPUT, str(answer))
    print('-'*30)


if __name__ == '__main__':
    task14()