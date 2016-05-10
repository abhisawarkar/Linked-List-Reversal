class Linkedlist:

	def __init__(self):
		self.head= None

	class Node:

		def __init__(self,d):
			self.data = d
			self.next= None

	def add_beg(self,data):
		New_node = self.Node(data)
		New_node.next = self.head
		self.head = New_node

	def add_end(self,data):
		New_node = self.Node(data)
		temp=self.head
		while temp.next != None:
			temp=temp.next		
		temp.next = New_node

	def reverse(self):
		temp=self.head
		New_LL=Linkedlist()
		while temp:
			N1=New_LL.Node(temp.data)
			N1.next=New_LL.head
			New_LL.head=N1
			temp=temp.next
		print New_LL.print_list()

	def print_list(self):
		temp=self.head
		while temp:
			print temp.data
			temp = temp.next 

LL=Linkedlist()
LL.add_beg(2)
LL.add_end(3)
LL.add_beg(8)
LL.add_end(1)
LL.print_list()
print "Reversing now"
LL.reverse()



		

