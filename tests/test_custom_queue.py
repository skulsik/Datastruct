from utils.custom_queue import *
import unittest


class Queue(unittest.TestCase):
    # Создаем экземпляр
    queue = Queue()
    # Заполняем очередь
    queue.enqueue('текст')
    queue.enqueue(777)
    queue.enqueue(True)


    def test_enqueue(self):
        """
        Проверка с подачей значения в data
        :return:
        """
        self.assertEqual(self.queue.head.data, 'текст')
        self.assertEqual(self.queue.head.next.data, 777)
        self.assertEqual(self.queue.tail.data, True)
        self.assertEqual(self.queue.tail.next, None)
