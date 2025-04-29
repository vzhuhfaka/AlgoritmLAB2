import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab3.utils import read_data, print_data


def task9(edges) -> bool:
    """
    Реализация алгоритма Беллмана-Форда для решения задачи
    :param edges: tuple
    :return: bool
    """
    if not edges:
        return False

    # Получаем все вершины графа
    vertices = set()
    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)
    n = len(vertices)

    # Инициализация расстояний
    dist = {v: float('inf') for v in vertices}

    # Начальная вершина
    start_vertex = next(iter(vertices))
    dist[start_vertex] = 0

    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Проверка на наличие отрицательных циклов
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            return True

    return False


def main() -> None:
    """
    Функция собирающая и обрабатывающая все данные
    """
    # Входные данные
    PATH_INPUT = 'lab3/task9/txtf/input.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    edges = []
    for line in data[1:]:
        if line:
            u, v, w = map(int, line.split())
            edges.append((u, v, w))

    # Обработка
    answer = task9(edges)

    # Данные о задаче
    print_data(number_lab=3, number_task=9, input_data=edges, output_data=answer)
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()