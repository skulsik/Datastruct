from utils.linked_list import *
import unittest
import HtmlTestRunner


class Test_Node(unittest.TestCase):
    def test_Node_not_next(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        node_test = Node(5)
        self.assertEqual(node_test.data, 5)
        self.assertEqual(node_test.next, None)


class Test_LinkedList(unittest.TestCase):
    @property
    def data(self):
        # Создаем экземпляр
        ll = LinkedList()
        # Заполняем список
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end()
        ll.insert_beginning({'id': 0})
        return ll


    def test_insert_beginning_and_end(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        self.assertEqual(self.data.head.data, {'id': 0})
        self.assertEqual(self.data.head.next.data, {'id': 1})
        self.assertEqual(self.data.tail.data, {})
        self.assertEqual(self.data.tail.next, None)


    def test_insert_end(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        tt = LinkedList()
        tt.insert_at_end({'id': 999})
        tt.insert_at_end({'id': 777})
        self.assertEqual(tt.head.data, {'id': 999})


    def test_data_none(self):
        """
        Проверка без значения в data
        :return:
        """
        rr = LinkedList()
        self.assertEqual(rr.print_ll(), None)


    def test_to_list(self):
        """
        Проверка на введенные данные
        :return:
        """
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.to_list, [{'id': 0, 'username': 'serebro'},
                                      {'id': 1, 'username': 'lazzy508509'},
                                      {'id': 2, 'username': 'mik.roz'},
                                      {'id': 3, 'username': 'mosh_s'}])


    def test_to_list_no_data(self):
        """
        Проверка на введенные данные
        :return:
        """
        ll = LinkedList()
        self.assertEqual(ll.to_list, [])


    def test_get_data_by_id(self):
        """
        Проверка на введенные данные
        :return:
        """
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll2.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll2.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})


    def test_get_data_by_id_error1(self):
        """
        Проверка на введенные данные с неверным id
        :return:
        """
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll2.get_data_by_id(2), {'id': 'не найден'})


    def test_get_data_by_id_error2(self):
        """
        Проверка на неверно введенные данные
        :return:
        """
        ll2 = LinkedList()
        ll2.insert_at_end('idusername')
        ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll2.get_data_by_id(2)
        self.assertEqual(str(ll2.error_dict_id), 'DictIdError: Данные не являются словарем или в словаре нет id.')
