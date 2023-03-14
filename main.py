from utils.Stack import *
from utils.custom_queue import *
from utils.linked_list import *


# Проверка логики по ТЗ-1
# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# print(n2.next)
#
# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# stack.push('data3')
# print(stack.top.data)
# print(stack.top.next.data)
# print(stack.top.next.next.data)
# print(stack.top.next.next.next)
# print(stack.top.next.next.next.data)


# Проверка логики по ТЗ-2
# stack = Stack()
# stack.push('data1')
# data = stack.pop()
#
# print(stack.top)
#
# print(data)
#
# stack1 = Stack()
# stack1.push('data1')
# stack1.push('data2')
# data = stack1.pop()

# теперь последний элемента содержит данные data1
# print(stack1.top.data)

# данные удаленного элемента
# print(data)


# ТЗ-3
# Создает экземпляр
# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
# queue.enqueue('data4')
# queue.enqueue('data5')
#
# print(queue.head.data)
# print(queue.head.next.data)
# print(queue.head.next.next.data)
# print(queue.tail.data)
# print(queue.tail.next)
# print(queue.tail.next.data)


# ТЗ-4
# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

# ТЗ-5
# ll = LinkedList()
# ll.insert_beginning({'id': 1})
# ll.insert_at_end({'id': 2})
# ll.insert_at_end({'id': 3})
# ll.insert_beginning({'id': 0})
# ll.print_ll()

# ТЗ-6
ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})

# метод to_list()
lst = ll.to_list
for item in lst:
    print(item)

# get_data_by_id()
user_data = ll.get_data_by_id(3)
print(user_data)

# работа блока try/except
ll2 = LinkedList()
ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll2.insert_at_end('idusername')
ll2.insert_at_end([1, 2, 3])
ll2.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll2.get_data_by_id(2)
print(user_data)
