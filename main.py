class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.item = -1

        while True:  # Крутит цикл пока не уберет все вложенные list
            stop = True
            self.flat_list = []
            for i in self.nested_list:
                if isinstance(i, list):
                    self.flat_list.extend(i)
                else:
                    self.flat_list.append(i)
            for i in self.flat_list:
                if isinstance(i, list):
                    stop = False
                    self.nested_list = self.flat_list
                    break
            if stop is True:
                break

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
        ['a', ['a', 'b', 'c'], 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        2
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


def flat_generator(nested_list):
    """generator"""

    item = 0
    while True:  # Крутит цикл пока не уберет все вложенные list
        stop = True
        flat_list = []
        for i in nested_list:
            if isinstance(i, list):
                flat_list.extend(i)
            else:
                flat_list.append(i)
        for i in flat_list:
            if isinstance(i, list):
                nested_list = flat_list
                stop = False
        if stop is True:
            break

    while item < len(flat_list):
        yield flat_list[item]
        item += 1


def generator_test():
    """Generator test function"""

    nested_list = [
        ['a', ['d', 'e', ['d', 'e', 'f']], 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
        2
    ]
    for item in flat_generator(nested_list):
        print(item)


def main():
    """Main function"""

    # iterator_test()  # Задача 1
    # generator_test()  # Задача 2


if __name__ == '__main__':
    main()
