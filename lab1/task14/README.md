# Задание №14 : `Максимальное значение арифметического выражения (2 балла)`

Студент ИТМО, Останин Андрей Сергеевич 466977

## Задание

В этой задаче ваша цель - добавить скобки к заданному арифметическому
выражению, чтобы максимизировать его значение. <br>
max(5 − 8 + 7 × 4 − 8 + 9) =?

## Input / Output

| Input       | Output |
|-------------|--------|
| 5-8+7*4-8+9 | 200    | 

## Ограничения по времени и памяти

- Ограничение по времени. 5 сек.

## Вопросы к задаче
1. Как алгоритм справляется с отрицательными значениями? <br>
Алгоритм работает корректно, из-за того, что рассматривает как минимальные,
так и максимальные значения в каждом этапе, в функции MinAndMax рассматриваются
все возможные случаи, включая отрицательные значения.<br><br>
2. Что происходит, если входное выражение содержит только одно число? <br>
Алгоритм просто возвратит это число как, одновременно, максимальное и
минимальное значение, просто не будет операций для выполнения.<br><br>
3. Какова временная сложность данного алгоритма? <br>
Временная сложность n^3, потому в коде имеется 3 вложенных цикла.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/vzhuhfaka/AlgoritmLAB2.git
   ```
2. Запустите программу:
   ```bash
   cd ../..
   python3 lab1/task14/src/task14.py
   ```
