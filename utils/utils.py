class Node:
    def __init__(self, data, next=None):
        """
        Узел стыка ячеек в стэке
        :param data: значение любого типа
        :param next: контейнер для следующего экземпляра
        """
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        """
        Инициализация головы стэка с пустым значением
        """
        self.top = None


    def push(self, data):
        """
        Механизм передачи предидущего экземпляра -> текущему (созданному)
        :param data: значение любого типа
        :return:
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        """
        Удаление последнего элемента стэка
        :return: Возврат значения последнего элемента
        """
        data = self.top.data
        self.top = self.top.next
        return data
