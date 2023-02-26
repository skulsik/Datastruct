class Node:
    def __init__(self, data, next=None):
        """
        Узел стыка ячеек в стэке
        :param data: значение любого типа
        :param next: контейнер для следующего экземпляра
        """
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        """
        Инициализация головы стэка с пустым значением
        """
        self.head = None
        self.tail = None


    def enqueue(self, data):
        """
        Добавление объекта в очередь
        :param data: Любое значение
        :return:
        """
        node = Node(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
