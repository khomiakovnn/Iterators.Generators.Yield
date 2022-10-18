class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.flat_list = []
        self.item = -1
        for i in self.nested_list:
            if isinstance(i, list):
                self.flat_list.extend(i)
            else:
                self.flat_list.append(i)  # Заготовка под задачу со *

    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        if self.item == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.item]


def iterator_test():
    """Iterator test function"""

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


def flat_generator(nested_list):
    """generator"""

    item = 0
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)  # Заготовка под задачу со *
    while item < len(flat_list):
        yield flat_list[item]
        item += 1


def generator_test():
    """Generator test function"""

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)


def main():
    """Main function"""

    # iterator_test() # Задача 1
    # generator_test() # Задача 2


if __name__ == '__main__':
    main()
