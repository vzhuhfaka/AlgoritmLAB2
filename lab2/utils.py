def read_data(path_file: str) -> list:
    with open(path_file, 'r') as f:
        return f.readlines()

def write_data(path_file: str, text: str) -> None:
    with open(path_file, 'w') as f:
        f.write(text)

def print_data(number_lab: int, number_task: int, input_data, output_data) -> None:
    print(f'Лабораторная: {number_lab} Задача: {number_task}\n'
          f'Входные данные: {input_data}\n'
          f'Вывод: {output_data}\n'
          f'{'-' * 30}')

__all__ = ['read_data', 'write_data']
