from utils.custom_queue import *
import unittest


class Test_Queue(unittest.TestCase):
    def data(self):
        # Создаем экземпляр
        queue = Queue()
        # Заполняем очередь
        queue.enqueue('текст')
        queue.enqueue(777)
        queue.enqueue(True)
        return queue


    def test_enqueue(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        self.assertEqual(self.data().head.data, 'текст')
        self.assertEqual(self.data().head.next.data, 777)
        self.assertEqual(self.data().tail.data, True)
        self.assertEqual(self.data().tail.next, None)


    def test_dequeue(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        Q_object = self.data()
        self.assertEqual(Q_object.dequeue(), 'текст')
        self.assertEqual(Q_object.dequeue(), 777)
        self.assertEqual(Q_object.dequeue(), True)
        self.assertEqual(Q_object.dequeue(), None)
