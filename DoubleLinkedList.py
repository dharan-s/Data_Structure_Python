class Node(object):
	def __init__(self, value):
		self.info = value
		self.prev = None
		self.next = None
		
class DoubleLinkedList(object):
	def __init__(self):
		self.start = None
		
	def display_list(self):
		if self.start is None:
			print("List is empty")
			return 
		
		print("List is : ")
		p = self.start
		while p is not None:
			print(p.info," ", end='')
			p = p.next
		print()
		
	def insert_at_beginning(self, data):
		if self.start is None:
			self.insert_in_empty_list(data)
			return 
		temp = Node(data)
		temp.next = self.start
		self.start.prev = temp 
		self.start = temp
		return 
	
	def insert_at_end(self, data):
		if self.start is None: #Node is empty 
			self.insert_in_empty_list(data)
			return
		temp = Node(data)
		p=self.start
		while p.next is not None:
			p = p.next
		p.next = temp
		temp.prev = p
		return
		
	def insert_in_empty_list(self, data):
		temp = Node(data)
		self.start = temp
		return 
		
	def insert_after(self, data, x):
		if self.start is None:
			print("List is empty")
			return
		p = self.start
		while p is not None:
			if p.info == x:
				break
			p = p.next
		if p is None:
			print("Elemet ", x ," is not present in list ")
			return
		temp = Node(data)
		if p.next is None: # last node
			temp.prev = p
			p.next = temp
		else:
			temp.next = p.next
			temp.prev = p
			p.next.prev = temp
			p.next = temp
		return
		
	def insert_before(self, data, x):
		if self.start is None:
			print("List is empty")
			return
		p = self.start
		while p is not None:
			if p.info == x:
				break
			p = p.next
		if p is None:
			print("Elemet ", x ," is not present in list ")
			return
		temp = Node(data)
		if p.prev is None: # first node
			temp.next = p
			p.prev = temp
			self.start = temp
		else:
			temp.next = p
			temp.prev = p.prev
			p.prev.next = temp
			p.prev = temp
		return		
	
	def delete_first_node(self):
		if self.start is None:
			print("List is empty")
			return
		if self.start.next is None:  #only one node is present
			self.start = None
		else:
			self.start = self.start.next
			self.start.prev = None
		return 
		
	def delete_last_node(self):
		if self.start is None:
			print("List is empty")
			return
		if self.start.next is None:
			self.start = None
		else:
			p = self.start
			while p.next is not None:
				p = p.next
			p.prev.next = None
		return
	
	
	def delete_node(self,x):
		if self.start is None:
			print("List is empty")
			return
		if self.start.next is None:
			if self.start.info == x:
				self.start = None
			else:
				print(x ," is not present in the list")
			return
		if self.start.info == x:
			self.delete_first_node()
			return 
		p = self.start
		while p is not None:
			if p.info == x:
				if p.next is None:
					p.prev.next = None
				else:
					p.next.prev = p.prev
					p.prev.next = p.next
				return
			p = p.next
		if p is None:
			print(x, " is not present")
	
	def reverse_list(self):
		if self.start is None:
			return
			
		p1 = self.start
		p2 = p1.next
		p1.next=None
		p1.prev = p2
		
		while p2 is not None:
			p2.prev = p2.next
			p2.next = p1
			p1 = p2 
			p2 = p2.prev
		self.start = p1 
		
	
	def create_list(self):
		n = int(input("Enter the number of nodes : "))
		if n == 0:
			return 
		data = int(input("Enter the first element to be inserted : "))
		self.insert_in_empty_list(data)
		
		for i in range(n-1):
			data = int(input("Enter the next element to be inserted : "))
			self.insert_at_end(data)
		
		
######################################################################################################

list = DoubleLinkedList()
list.create_list()

while True:
	print("1. Display List")
	print("2. Count the number of Nodes")
	print("3. Insert a node in a empty list")
	print("4. Insert a node at beginning of a list ")
	print("5. Insert a node at the end of a list")
	print("6. Insert a node after a specified node")
	print("7. Insert a node before a specified node")
	print("8. Insert a node at a given position")
	print("9. Delete first node")
	print("10. Delete last node")
	print("11. Delete any node")
	print("12. Reverse the list")
	print("13. Quit")
	
	option = int(input("Enter your choice : "))
	
	if(option == 1):
		list.display_list()
	elif(option == 2):
		list.count_nodes()
	elif(option == 3):
		data = int(input("Enter the element to be inserted  : "))
		list.insert_at_beginning(data)
	elif(option == 4):
		data = int(input("Enter the element to be inserted : "))
		list.insert_at_beginning(data)
	elif(option == 5):
		data = int(input("Enter the element to be inserted : "))
		list.insert_at_end(data)
	elif(option == 6):
		data = int(input("Enter the element to be inserted : "))
		x = int(input("Enter the element after which to insert : "))
		list.insert_after(data,x)
	elif(option == 7):
		data = int(input("Enter the element to be inserted : "))
		x = int(input("Enter the element before which to insert : "))
		list.insert_before(data,x)
	elif(option == 8):
		data = int(input("Enter the element to be inserted : "))
		k = int(input("Enter the position at which to insert : "))
		list.insert_at_position(data,k)
	elif(option == 9):
		list.delete_first_node()
	elif(option == 10):
		list.delete_last_node()
	elif(option == 11):
		data = int(input("Enter the element to be deleted : "))
		list.delete_node(data)
	elif(option == 12):
		list.reverse_list()
	elif(option == 13):
		break
	else:
		print("Wrong option")
	
	print()
		