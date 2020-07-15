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
		# create new node with passed in value
		new_node = ListNode(value)
		# check for empty list and make new node head and tail if it is
		if self.check_for_empty_list():
			self.head = new_node
			self.tail = new_node
		# assign new node to self.head
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
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		self.length -= 1
		# pull value out of head before removing it
		value = self.head.value
		# check if there is only one item in list and delete it if true
		if not self.head.next:
			self.head = None
			self.tail = None
			return value
		# otherwise assign new head and return the value
		self.head = self.head.next
		return value

	"""
	Wraps the given value in a ListNode and inserts it
	as the new tail of the list. Don't forget to handle
	the old tail node's next pointer accordingly.
	"""
	def add_to_tail(self, value):
		# create new node with passed in value
		new_node = ListNode(value)
		# check for empty list and make new node head and tail if it is
		if self.check_for_empty_list():
			self.head = new_node
			self.tail = new_node
		# assign new node to self.tail
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
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		self.length -= 1
		# pull value out of head before removing it
		value = self.tail.value
		# check if there is only one item in list and delete it if true
		if not self.tail.prev:
			self.head = None
			self.tail = None
			return value
		# otherwise assign new head and return the value
		self.tail = self.tail.prev
		return value

	"""
	Removes the input node from its current spot in the
	List and inserts it as the new head node of the List.
	"""
	def move_to_front(self, node):
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		# check if there is only one node in list
		if (not node.next) and (not node.prev):
			return
		# check if the node is already at the front
		elif (node.next) and (not node.prev):
			return
		# check if node is in the middle and then change the next and prev attr
		# for the nodes around the one being moved
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
		# check if node is the tail and change self.tail
		elif (not node.next) and (node.prev):
			node.prev.next = None
			self.tail = node.prev
		# move node to the front/assign it to self.head
		node.prev = None
		node.next = self.head
		self.head.prev = node
		self.head = node

	"""
	Removes the input node from its current spot in the
	List and inserts it as the new tail node of the List.
	"""
	def move_to_end(self, node):
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		# check if there is only one node in list
		if (not node.next) and (not node.prev):
			return
		# check if the node is already at the end
		elif (not node.next) and (node.prev):
			return
		# check if node is in the middle and then change the next and prev attr
		# for the nodes around the one being moved
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
		# check if node is the head and change self.head
		elif (node.next) and (not node.prev):
			node.next.prev = None
			self.head = node.next
		# move node to the end/assign it to self.tail
		node.next = None
		node.prev = self.tail
		self.tail.next = node
		self.tail = node

	"""
	Deletes the input node from the List, preserving the
	order of the other elements of the List.
	"""
	def delete(self, node):
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		# pull value out of node before removing it
		value = node.value
		# check if there is only one item in list and delete it if true
		if (not node.next) and (not node.prev):
			self.head = None
			self.tail = None
		# check if node is in the middle and then change the next and prev attr
		# for the nodes around the one being moved
		elif (node.next) and (node.prev):
			node.prev.next = node.next
			node.next.prev = node.prev
			node.next = None
			node.prev = None
		# check if node is the head and change self.head
		elif (node.next) and (not node.prev):
			node.next.prev = None
			self.head = node.next
		# check if node is the tail and change self.tail
		elif (not node.next) and (node.prev):
			node.prev.next = None
			self.tail = node.prev
		# get rid of node value
		node.value = None
		self.length -= 1
		return value

	"""
	Finds and returns the maximum value of all the nodes
	in the List.
	"""
	def get_max(self):
		# check if list is empty and return none if it is
		if self.check_for_empty_list():
			return None
		# assign value of head to max variable
		max = self.head.value
		# assign head to node variable
		node = self.head
		# loop through length of list
		for i in range(1, self.length):
			# change node being looked at to the next
			node = node.next
			# update max value when needed
			if node.value > max:
				max = node.value
		return max

	def check_for_empty_list(self):
		# check if the head and tail exist
		# if not return True - list is empty
		# if yes return False - list is not empty
		if (not self.head) and (not self.tail):
			return True
		else:
			return False
