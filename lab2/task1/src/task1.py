import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab2.utils import read_data, print_data


class Node:
    """
    Класс узла двоичного дерева
    """
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def init_tree(data, i):
    """
    Инициализация двоичного дерева
    """
    if i == -1:
        return None
    node = Node(data[i][0], init_tree(data, data[i][1]), init_tree(data, data[i][2]))
    return node


def in_order(node):
    """
    Обход in_order
    """
    if node is None:
        return
    in_order(node.left)
    print(node.key, end=' ')
    in_order(node.right)


def pre_order(node):
    """
    Обход pre_order
    """
    if node is None:
        return None
    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    """
    Обход post_order
    """
    if node is None:
        return None
    post_order(node.left)
    post_order(node.right)
    print(node.key, end=' ')


def task1(data):
    """
    Выполнение задачи
    """
    data = data[1:]
    node = init_tree(data, 0)
    in_order(node)
    print('')
    pre_order(node)
    print('')
    post_order(node)


def main():
    """
    Функция собирающая и обрабатывающая все данные
    """
    # Входные данные
    PATH_INPUT = 'lab2/task1/txtf/input.txt'
    PATH_OUTPUT = 'lab2/task1/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    format_data = [[int(i) for i in j.split()] for j in data]

    print_data(number_lab=2, number_task=1, input_data=format_data, output_data='')
    task1(format_data)
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()