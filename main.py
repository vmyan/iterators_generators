class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iteration = iter(self.list_of_list)
        self.nested_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iteration)
        return self.nested_list[self.cursor]


def flat_generator(my_list):
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('Вызов итератора')
    for item in FlatIterator(nested_list):
        print(item)
    print('_' * 30)

    print('Вызов генератора списка (comprehension)')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('_' * 30)

    print('Вызов генератора')
    for item in flat_generator(nested_list):
        print(item)