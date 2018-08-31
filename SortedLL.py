#SortedLinkedList.py 
#   Implementing the sorted linke list with insert, search function

class Node():
	def __init__(self,value):
		self.info = value 
		self.link = None
		
class SortedLinkedList():

	def __init__(self):
		self.start = None
		
	def display_list(self):
		if self.start is None:
			print("List is empty")
		p = self.start 
		while p is not None:
			print(p.info, " " ,end='')
			p = p.link
		print()
		
	def insert_data_in_order(self, data):
		temp = Node(data)
		
		if self.start is None or self.start.info >= data:
			temp.link = self.start
			self.start = temp
			return 
		
		p = self.start 
		while p.link is not None and p.link.info <= data:
			p = p.link
		#if p is not None:
		temp.link = p.link 
		p.link = temp
		
	def create_list(self):
		n = int(input("Enter no of nodes : "))
		if n == 0:
			return
		for i in range(n):
			data = int(input("Enter the value to be inserted : "))
			self.insert_data_in_order(data)
		
	def search(self, data):
		if self.start is None:
			print("List is empty ")
			return
		
		p = self.start
		position = 1
		while p is not None and p.info <= data:
			if p.info == data:
				break
			p = p.link
		
		if p is None or p.info != data:
			print(data, " not present in the list")
		else:
			print(data, " is in position ", position)
			
			
	def delete(self, x):
		if self.start is None:
			print("List is empty")
			return 
			
		if self.start.info == x:
			if self.start.link is None:
				self.start = None
			else:	
				self.start = self.start.link
			return
		
		p = self.start
		while p.link is not None and p.link.info <= x:
			if p.link.info == x:
				p.link = p.link.link
				return 
				
		print(x, " not present in the list ")		
				
###############################################

list = SortedLinkedList()
list.create_list()

while True:
	print("#-------------SortedLinkedList-------------#")
	print("1. Display List")
	print("2. Insert a node")
	print("3. Search a node")
	print("4. Delete a node")
	print("5. Quit")
	
	option = int(input("Enter your choice : "))
	
	if(option == 1):
		list.display_list()
	elif(option == 2):
		data = int(input("Enter the element to be inserted  : "))
		list.insert_data_in_order(data)
	elif(option == 3):
		data = int(input("Enter the element to be inserted  : "))
		list.search(data)
	elif(option == 4):
		data = int(input("Enter the element to be inserted : "))
		list.delete(data)
	elif(option == 5):
		break