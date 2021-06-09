class Node:

	def __init__(self, value:int):
		self.value = value
		self.next = None

	def __str__(self) -> int:
		return self.value

class LinkedList:
	
	def __init__(self, value:int):
		node = Node(value)
		self.start = node

	def append(self, value:int):
		"""
		Adds a node at the end of LinkedList.
		"""

		print(f"Appending {value}")
		node = Node(value)
		temp = self.start

		if not temp:
			# append node in empty list
			self.start = node
			return

		while temp.next:
			temp = temp.next

		temp.next = node

	def prepend(self, value:int):
		"""
		Adds a node at the start of LinkedList.
		"""

		print(f"Prepending {value}")
		node = Node(value)

		temp = self.start
		if not temp:
			# append node in empty list
			self.start = node
			return

		node.next = self.start
		self.start = node

	def delete_first(self):
		"""
		Removes a node from the start of LinkedList.
		"""

		print("Deleting first node")
		if not self.start:
			print('cannot delete from empty list')
			return

		self.start = self.start.next

	def delete_last(self):
		"""
		Removes a node from the end of LinkedList.
		"""

		print("Deleting last node")
		if not self.start:
			print('cannot delete from empty list')
			return

		temp = self.start

		# if LinkedList has only single node
		if temp.next == None:
			self.start = None
			return

		while temp.next.next:
			temp = temp.next

		# update next of second last node to delete node
		temp.next = None

	def delete_by_value(self, value:int):
		"""
		Removes the first node from LinkedList which matches the value.
		"""

		print(f"Deleting node with value: {value}")
		if not self.start:
			print('cannot delete from empty list')
			return

		if self.start and self.start.value == value:
			self.delete_first()
			return

		temp = self.start
		matching_node_exists = False
		while temp.next:
			if temp.next.value == value:
				matching_node_exists = True
				break

			temp = temp.next

		if matching_node_exists:
			# delete the node with matching value
			temp.next = temp.next.next
		else:
			print(f"node with value: {value} not found")

	def display(self):
		print("Linked List: ", end='')
		if not self.start:
			print('Empty list\n')
			return
		
		temp = self.start
		while temp:
			print(f'{temp.value} -> ', end='')
			temp = temp.next

		print('\n')

def main():
	ll = LinkedList(1)
	ll.display()

	ll.delete_first()
	ll.display()

	ll.delete_first()
	ll.display()

	# return

	ll.append(2)
	ll.append(3)

	ll.display()

	ll.delete_last()
	ll.display()

	ll.delete_first()
	ll.display()

	ll.prepend(4)
	ll.display()

	ll.append(10)
	ll.display()

	ll.append(5)
	ll.display()

	ll.delete_by_value(10)
	ll.display()

	ll.delete_by_value(10)
	ll.display()

	ll.delete_last()
	ll.display()

	print("Final Linked List")
	ll.display()


if __name__ == '__main__':
	main()