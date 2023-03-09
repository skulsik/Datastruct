class Node:
    def __init__(self, data: dict, next: object = None):
        """
        Узел стыка ячеек в списке
        :param data: значения типа dict
        :param next: контейнер для следующего экземпляра
        """
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """Инициализыция переменных"""
        self.head = None
        self.tail = None


    def insert_beginning(self, data_dict: dict = {}):
        """Добавление словаря в голову списка"""
        node = Node(data_dict)
        if self.head is None:
            self.tail = node
        node.next = self.head
        self.head = node


    def insert_at_end(self, data_dict: dict = {}):
        """Добавление словаря в хвост списка"""
        node = Node(data_dict)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node


    def print_ll(self):
        """Вывод списка"""
        ll_string: str = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        print(ll_string)
