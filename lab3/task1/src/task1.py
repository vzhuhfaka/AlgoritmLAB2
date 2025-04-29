import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab3.utils import read_data, print_data


class Node:
    """
    Узел графа
    """
    def __init__(self, key):
        self.children = []
        self.key = key

    def add(self, node):
        """
        Добавляет в узел соседние узлы
        :param node: Node() object
        :return: None
        """
        self.children.append(node)


def init_graph(data) -> dict:
    """
    Создается граф, узлы которого хранятся в словаре вида
    :param data: list[list]
    :return: dict
    """
    graph = {}
    for i in range(len(data)):
        key = data[i][0]
        childrenKey = data[i][1]
        childrenNode = Node(childrenKey)
        if key not in graph.keys():
            graph[key] = Node(key)
            graph[key].add(childrenNode)
        else:
            graph[key].add(childrenNode)

    return graph


def print_graph(graph) -> None:
    """
    Печатает граф в удобочитаемом формате
    :param graph: dict
    :return: None
    """
    print("\nГраф:")
    for node in graph.values():
        # Выводим текущую вершину
        print(f"[{node.key}] -> ", end="")

        # Выводим всех соседей
        if not node.children:
            print("нет соседей")
        else:
            neighbors = [child.key for child in node.children]
            print(str(neighbors))


def findPath(graph, start, end) -> bool:
    """
    Проверяет наличие пути между start и end
    :param graph: dict
    :param start: int
    :param end: int
    :return: bool
    """
    if start == end:
        return True

    if start not in graph.keys():
        return False

    childs = graph[start].children

    if childs:
        for i in childs:
            current = i.key
            if findPath(graph, current, end):
                return True

    return False


def task1(data, target) -> bool:
    """
    Обработка всех данных
    :param data: list[list]
    :param target: [int, int]
    :return: bool
    """
    graph = init_graph(data)
    start = target[0]
    end = target[1]
    isPath = findPath(graph, start, end)
    return isPath


def main() -> None:
    """
    Функция собирающая и обрабатывающая все данные
    """
    # Входные данные
    PATH_INPUT = 'lab3/task1/txtf/input.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    # example: [['4', '4'], ['1', '2']] -> [[4, 4], [1, 2]]
    format_data = [[int(j) for j in i.split()] for i in data[1:]]
    target = format_data[-1]

    # Обработка
    answer = task1(format_data[:-1],
          target)  # срезаем у format_data последний элемент, так как последний элемент - это start и end

    # Данные о задаче
    print_data(number_lab=3, number_task=1, input_data=format_data, output_data=answer)
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()