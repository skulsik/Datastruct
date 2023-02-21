from utils.utils import *
import unittest


class Test_Node(unittest.TestCase):
    def test_Node_not_next(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        node_test = Node(5)
        self.assertEqual(node_test.data, 5)
        self.assertEqual(node_test.next, None)


    def test_Node(self):
        """
        Проверка с подачей значения в data и присваивание экземпляра в next
        :return:
        """
        node_test = Node("opa")
        node_test2 = Node(True, node_test)
        self.assertEqual(node_test.data, "opa")
        self.assertEqual(node_test.next, None)
        self.assertEqual(node_test2.data, True)
        self.assertEqual(node_test2.next, node_test)


class Test_Stack(unittest.TestCase):
    # Создаем экземпляр
    stack = Stack()
    # Заполняем стек
    stack.push(777)
    stack.push('текст')
    stack.push(True)


    def test_push(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        self.assertEqual(self.stack.top.data, 'текст')
        self.assertEqual(self.stack.top.next.next, None)


    def test_pop(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        self.assertEqual(self.stack.pop(), True)
