from utils.utils import *


# Проверка логики по ТЗ
n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next.data)
print(stack.top.next.next.data)
print(stack.top.next.next.next)
#print(stack.top.next.next.next.data)
