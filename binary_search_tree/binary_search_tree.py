"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
	on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
	on the BSTNode class.
"""
class BSTNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):
		# if value < current node value
		if value < self.value:
			# check if left attr node is none and if it is
			# create a new node with the passed in value
			if self.left is None:
				self.left = BSTNode(value)
			# otherwise call insert function on left attr node
			else:
				self.left.insert(value)
		# check if value >= current node value
		else:
			# check if right attr node is none and if it is
			# create a new node with the passed in value
			if self.right is None:
				self.right = BSTNode(value)
			# otherwise call insert function on right attr node
			else:
				self.right.insert(value)

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		# if target value equals current node value return true
		if target == self.value:
			return True
		# check if target < current node value
		elif target < self.value:
			# if left attr node is none return false
			if self.left is None:
				return False
			# otherwise return contains function call on left attr node
			else:
				return self.left.contains(target)
		# check if target >= current node value
		else:
			# if right attr node is none return false
			if self.right is None:
				return False
			# otherwise return contains function call on right attr node
			else:
				return self.right.contains(target)

	# Return the maximum value found in the tree
	def get_max(self):
		# if right side of tree is none - meaning there are no
		# greater values than current node value - return current node value
		if self.right is None:
			return self.value
		# otherwise return get_max function call on right attr node
		else:
			return self.right.get_max()

	# Call the function `fn` on the value of each node
	def for_each(self, fn):
		# call function on current node value
		fn(self.value)
		# if left attr is not none call for_each function on left attr node
		if self.left is not None:
			self.left.for_each(fn)

		# if right attr is not none call for_each function on right attr node
		if self.right is not None:
			self.right.for_each(fn)

	# Part 2 -----------------------

	# Print all the values in order from low to high
	# Hint:  Use a recursive, depth first traversal
	def in_order_print(self, node):
		pass

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self, node):
		pass

	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self, node):
		pass

	# Stretch Goals -------------------------
	# Note: Research may be required

	# Print Pre-order recursive DFT
	def pre_order_dft(self, node):
		pass

	# Print Post-order recursive DFT
	def post_order_dft(self, node):
		pass
