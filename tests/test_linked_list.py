from utils.linked_list import *
import unittest
import HtmlTestRunner


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
