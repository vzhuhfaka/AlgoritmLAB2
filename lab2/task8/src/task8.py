import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab2.utils import read_data, print_data, write_data


class Node:
    """
    Класс узла бинарного дерева
    """
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

        # Вычисляем максимальную высоту из левого и правого поддерева
        self.left_height = left.height if left else 0
        self.right_height = right.height if right else 0
        # Общая высота узла
        self.height = max(self.left_height, self.right_height) + 1


def init_tree(data, i):
    """
    Инициализация бинарного дерева
    :param data: [[6], [-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]
    :param i: индекс ребенка в data
    :return: Объект класса Node
    """
    if i == 0:
        return None
    node = Node(data[i][0], init_tree(data, data[i][1]), init_tree(data, data[i][2]))

    return node


def task8(data):
    """
    Выполнение задачи
    :param data: список с узлами дерева
    :return: высота дерева
    """
    data[0] = None
    tree = init_tree(data, 1)

    return tree.height


def main():
    """
    Функция собирающая и обрабатывающая все данные
    :return: None
    """
    # Входные данные
    PATH_INPUT = 'lab2/task8/txtf/input.txt'
    PATH_OUTPUT = 'lab2/task8/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]
    format_data = [[int(i) for i in j.split()] for j in data]

    # Обработка запросов
    results = task8(format_data)

    # Вывод результатов
    print_data(number_lab=2, number_task=8, input_data=format_data, output_data=results)
    print(f'\n{'-' * 30}')
    write_data(PATH_OUTPUT, str(results))


if __name__ == '__main__':
    main()