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
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    """
    Вставка нового ключа в BST
    """
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_min_greater(root, x):
    """
    Поиск минимального элемента, большего x
    """
    current = root
    result = 0
    while current:
        if current.key > x:
            result = current.key
            current = current.left
        else:
            current = current.right
    return result


def init_tree(data):
    """
    Создание BST из списка данных
    :param data: список значений, например [0, 43, 2, 4, 29, 13]
    :return: корень дерева
    """
    root = None
    for item in data:
        root = insert(root, item)
    return root


def task3(data):
    """
    Обработка запросов и построение BST
    :param data: список запросов, например [["+", 1], [">", 2]]
    :return: список результатов для запросов вида ">"
    """
    root = None
    results = []
    for command, value in data:
        if command == '+':
            if root is None:
                root = Node(value)
            else:
                insert(root, value)
        elif command == '>':
            result = find_min_greater(root, value)
            results.append(result)
    return results


def main():
    # Входные данные
    PATH_INPUT = 'lab2/task3/txtf/input.txt'
    PATH_OUTPUT = 'lab2/task3/txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]
    format_data = [[i.split()[0], int(i.split()[1])] for i in data]  # example "+ 2" -> ["+", 2]

    # Обработка запросов
    results = task3(format_data)

    # Вывод результатов
    print_data(number_lab=2, number_task=1, input_data=format_data, output_data=results)
    print(f'\n{'-' * 30}')
    write_data(PATH_OUTPUT, str(results))

if __name__ == '__main__':
    main()