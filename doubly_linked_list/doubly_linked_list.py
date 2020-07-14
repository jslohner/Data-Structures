"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
	def __init__(self, value, prev=None, next=None):
		self.prev = prev
		self.value = value
		self.next = next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node
		self.length = 1 if node is not None else 0

	def __len__(self):
		return self.length

	"""
	Wraps the given value in a ListNode and inserts it
	as the new head of the list. Don't forget to handle
	the old head node's previous pointer accordingly.
	"""
	def add_to_head(self, value):
		new_node = ListNode(value)
		# if (not self.head) and (not self.tail):
		if self.check_for_empty_list():
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
		self.length += 1

	"""
	Removes the List's current head node, making the
	current head's next node the new head of the List.
	Returns the value of the removed Node.
	"""
	def remove_from_head(self):
		# if (not self.head) and (not self.tail):
		if self.check_for_empty_list():
			return None
		self.length -= 1
		value = self.head.value
		if not self.head.next:
			self.head = None
			self.tail = None
			return value
		self.head = self.head.next
		return value

	"""
	Wraps the given value in a ListNode and inserts it
	as the new tail of the list. Don't forget to handle
	the old tail node's next pointer accordingly.
	"""
	def add_to_tail(self, value):
		new_node = ListNode(value)
		if self.check_for_empty_list():
			self.head = new_node
			self.tail = new_node
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
		self.length += 1

	"""
	Removes the List's current tail node, making the
	current tail's previous node the new tail of the List.
	Returns the value of the removed Node.
	"""
	def remove_from_tail(self):
		if self.check_for_empty_list():
			return None
		self.length -= 1
		value = self.tail.value
		if not self.tail.prev:
			self.head = None
			self.tail = None
			return value
		self.tail = self.tail.prev
		return value

	"""
	Removes the input node from its current spot in the
	List and inserts it as the new head node of the List.
	"""
	def move_to_front(self, node):
		if self.check_for_empty_list():
			return None

		if (not node.next) and (not node.prev):
			return
		elif (node.next) and (not node.prev):
			return
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
		elif (not node.next) and (node.prev):
			node.prev.next = None
			self.tail = node.prev

		node.prev = None
		node.next = self.head
		self.head.prev = node
		self.head = node

	"""
	Removes the input node from its current spot in the
	List and inserts it as the new tail node of the List.
	"""
	def move_to_end(self, node):
		if self.check_for_empty_list():
			return None

		if (not node.next) and (not node.prev):
			return
		elif (not node.next) and (node.prev):
			return
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
		elif (node.next) and (not node.prev):
			node.next.prev = None
			self.head = node.next

		node.next = None
		node.prev = self.tail
		self.tail.next = node
		self.tail = node

	"""
	Deletes the input node from the List, preserving the
	order of the other elements of the List.
	"""
	def delete(self, node):
		if self.check_for_empty_list():
			return None
		value = node.value
		if (not node.next) and (not node.prev):
			self.head = None
			self.tail = None
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
			node.next = None
			node.prev = None
		elif (node.next) and (not node.prev):
			node.next.prev = None
			self.head = node.next
		elif (not node.next) and (node.prev):
			node.prev.next = None
			self.tail = node.prev
		# node.next = None
		# node.prev = None
		node.value = None
		self.length -= 1
		return value

	"""
	Finds and returns the maximum value of all the nodes
	in the List.
	"""
	def get_max(self):
		if self.check_for_empty_list():
			return None
		max = self.head.value
		node = self.head
		for i in range(1, self.length):
			node = node.next
			if node.value > max:
				max = node.value
		return max

	def check_for_empty_list(self):
		if (not self.head) and (not self.tail):
			return True
		else:
			return False
