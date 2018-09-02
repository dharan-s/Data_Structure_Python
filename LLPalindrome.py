class Node(object):
	def __init__(self, value):
		self.info = value
		self.next = None
		
		
class Pointer():
	def __init__(self):
		self.head = None
		self.tail = None 
		
	def insert_at_end(self, data): 
		temp = Node(data)
		if self.head is None:
			self.head = temp
			self.tail = temp 
		else:
			self.tail.next = temp 
			self.tail = temp
			
	def insert_at_end_notail(self, data):
		temp = Node(data)
		if self.head is None:
			self.head = temp
		else:
			p = self.head 
			while p.next is not None:
				p = p.next
			p.next = temp
		
	def display(self):
		if self.head is None:
			print("List is empty")
		else:
			p = self.head 
			while p is not None:
				print(p.info," ",end='')
				p = p.next 
			print()
			
	def create(self):
		num_nodes = int(input("Enter the number of nodes : "))
		for i in range(num_nodes):
			data = int(input("Enter data to be inserted : "))
			#self.insert_at_end(data)
			self.insert_at_end_notail(data)
			
	def tail_element(self):
		if self.head is not None:
			print(self.tail.info)
			
	def middle_last_element(self):
		if self.head is not None:
			p1 = self.head 
			p2 = self.head 
			while(p2.next):
				p1 = p1.next 
				p2 = p2.next
				if p2.next is not None:
					p2 = p2.next
			print("Middle element : ", p1.info)
			print("Last elemet : ", p2.info)
				
	def reverse(self):
		if self.head and self.head.next:
			prev = None 
			p = self.head
			while p is not None:
				next = p.next
				p.next = prev
				prev = p
				p = next	
			self.head = prev 
			
	def palindrome(self):
		if self.head and self.head.next:
			p = self.head 
			self.reverse()
			q = self.head 
			while p and q:
				if p.info != q.info:
					print("Not plaindrome")
					return
				p = p.next
				q = q.next
			print("Palindrome")	
		elif self.head is None :
			print("List is Empty")
		else:
			print("Palindrome")
			
######################

l = Pointer()
l.create()
l.display()
#l.tail_element()
#l.middle_last_element()
l.palindrome() 