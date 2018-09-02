# Stack Implementaion using Single Linked List
# StackLL.py

class Node(object):
	def __init__(self, value):
		self.info = value
		self.next = None

class StackEmptyError(Exception):
	pass
		
class StackLL(object):
	def __init__(self):
		self.head = None
	
	def is_emptyLL(self):
		return self.head == None
		
	def push(self, data):
		temp = Node(data)
		if self.is_emptyLL():
			self.head = temp
		else:
			temp.next = self.head
			self.head = temp
		
	def pop(self):
		if self.is_emptyLL():
			raise StackEmptyError("Stack is Empty")
		data = self.head.info
		self.head = self.head.next
		return data 
		
	def peek(self):
		if self.is_emptyLL():
			raise StackEmptyError("Stack is Empty")
		data = self.head.info
		return data 
	
	def display(self):
		if self.is_emptyLL():
			print("Stack is empty")
		else:
			p = self.head
			while p is not None:
				print(p.info , " " , end='')
				p = p.next
		print()
		
##############################################

if __name__ == "__main__":

	s = StackLL()
	
	while True:
		print("#-------------Simple Stack with max_size Implementation-----------------#")
		print("1. Display")
		print("2. Push")
		print("3. Pop")
		print("4. Peek")
		print("5. Quit")
		
		option = int(input("Enter your choice : "))
		
		if(option == 1):
			s.display()
		elif(option == 2):
			data = int(input("Enter the element to be pushed  : "))
			s.push(data)
		elif(option == 3):
			data = s.pop()
			print("Popped data is ", data)
		elif(option == 4):
			data = s.peek()
			print("Peeked data is ", data)
		elif(option == 5):
			break
		else:
			print("Invalid option")
