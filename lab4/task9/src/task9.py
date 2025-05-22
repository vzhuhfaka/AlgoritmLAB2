import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab4.utils import read_data, print_data


def find_repetitions(s):
    """
    Находит оптимальное сжатое представление строки, используя повторяющиеся подстроки и конкатенацию.
    """
    n = len(s)
    # Создаем DP-таблицу, где dp[i][j] хранит оптимальное представление подстроки s[i..j]
    dp = [["."] * n for _ in range(n)]  # Инициализация символом-заполнителем

    # Заполняем диагональ (подстроки длины 1) исходными символами
    for i in range(n):
        for j in range(i, n):
            dp[i][j] = s[i:j + 1]

    # Перебираем все возможные длины подстрок (от 1 до n)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # Конечный индекс подстроки

            substring = s[i:j + 1]
            dp[i][j] = substring

            # Проверяем, можно ли сжать подстроку как повторение более короткой подстроки
            for k in range(1, length):
                # Если длина подстроки делится на k, то возможно повторение
                if length % k == 0:
                    repeat_count = length // k
                    repeated_substring = s[i:i + k]
                    if repeated_substring * repeat_count == substring:
                        candidate = f"{repeated_substring}*{repeat_count}"

                        # Если кандидат короче текущего представления, обновляем DP-таблицу
                        if len(candidate) < len(dp[i][j]):
                            dp[i][j] = candidate

            # Проверяем, можно ли разбить подстроку на две части и сжать их отдельно
            for k in range(i, j):
                candidate = dp[i][k] + "+" + dp[k + 1][j]
                if len(candidate) < len(dp[i][j]):
                    dp[i][j] = candidate

    # Возвращаем оптимальное представление всей строки (s[0..n-1])
    return dp[0][n - 1]

def task1(data):
    s = data.strip()
    optimal_representation = find_repetitions(s)
    return optimal_representation

def main() -> None:
    """Функция собирающая и обрабатывающая все данные"""

    # Входные данные
    PATH_INPUT = 'lab4/task9/txtf/input.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]

    # Обработка
    answer = task1(data=data[0])

    # Данные о задаче
    print_data(number_lab=4, number_task=9, input_data=data, output_data=(len(answer), answer))
    print(f'\n{'-' * 30}')


if __name__ == '__main__':
    main()