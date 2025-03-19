from lab2.utils import read_data, write_data, print_data


class node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def in_order(self, root):
        if not root:
            return
        self.in_order(self.left)
        print(root.key)
        self.in_order(self.right)


def task1():
    pass


def main():
    # Входные данные
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    data = [i.strip() for i in read_data(PATH_INPUT)]


    print_data(number_lab=2, number_task=1, input_data='sssa', output_data='sdfws')


if __name__ == '__main__':
    main()