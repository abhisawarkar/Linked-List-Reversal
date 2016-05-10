class Linkedlist:

	def __init__(self):			# Initialize linked list
		self.head= None

	class Node:				

		def __init__(self,d):		# Initialize node
			self.data = d
			self.next= None

	def add_beg(self,data):			# Add node at beginning
		New_node = self.Node(data)
		New_node.next = self.head
		self.head = New_node

	def add_end(self,data):			# Add node at end
		New_node = self.Node(data)
		temp=self.head
		while temp.next != None:
			temp=temp.next		
		temp.next = New_node

	def reverse(self):			# Reverse a linked list
		temp=self.head
		New_LL=Linkedlist()
		while temp:
			N1=New_LL.Node(temp.data)
			N1.next=New_LL.head
			New_LL.head=N1
			temp=temp.next
		print New_LL.print_list()

	def print_list(self):			# Print
		temp=self.head
		while temp:
			print temp.data
			temp = temp.next 




		

