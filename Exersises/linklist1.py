class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new_node

	def display(self):
		values = []
		current = self.head

		while current is not None:
			values.append(str(current.data))
			current = current.next

		print(" -> ".join(values) if values else "Empty list")


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()
