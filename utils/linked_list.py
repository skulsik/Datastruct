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
        node: object = Node(data_dict)
        if self.head is None:
            self.tail = node
        node.next = self.head
        self.head = node


    def insert_at_end(self, data_dict: dict = {}):
        """Добавление словаря в хвост списка"""
        node: object = Node(data_dict)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node


    def print_ll(self):
        """Вывод списка в виде строки"""
        ll_string: str = ''
        node: object = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        print(ll_string)


    @property
    def to_list(self) -> list:
        """ Вывод списка в виде списка"""
        ll_list: list = []
        node: object = self.head
        while node:
            ll_list.append(node.data)
            node = node.next
        return ll_list

    def get_data_by_id(self, id: int) -> dict:
        """
        Поиск словаря по Id
        :param id: по которому следует найти словарь
        :return: возврат словаря найденого по id, либо сообщения ('id': 'не найден')
        """
        data_dict: dict = {'id': 'не найден'}
        node = self.head
        while node:
            try:
                # Проверка: на существование id в словаре; на принадлежность данных данного экземпляра к классу словаря
                if 'id' in node.data and isinstance(node.data, dict):
                    if node.data['id'] == id:
                        # присваивает переменной, иначе если сделать возврат, пройдет не по всем экземплярам
                        data_dict = node.data
                else:
                    raise DictIdError('DictIdError: Данные не являются словарем или в словаре нет id.')
            except DictIdError as e:
                self.error_dict_id: str = e
            node = node.next
        return data_dict


class DictIdError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'DictIdError: Неизвестная ошибка'
        print(self.message)


    def __str__(self):
        return self.message
