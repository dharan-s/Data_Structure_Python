#QueueLinkedList.py

#Insertion --> done at rear 
#deletion --> done at front 

class EmptyStackError(Exception):
	pass
	
class Node():
	def __init__(self, value):
		self.info = value
		self.next = None
		
class QueueLinkedList():
	def __init__(self):
		self.front = None
		self.rear = None
		
	def is_empty(self):
		return self.front == None 
	
	def display(self):
		if self.front is None: 
			print("List is empty")
		else:
			p = self.front 
			while p is not None:
				print(p.info, " ", end='')
				p = p.next
			print()
	
	def size(self):
		if self.front == None:
			print("Size is 0")
		elif self.front.next is None:
			print("Size is 1")
		else:
			p = self.front.next
			count = 1
			while p is not None:
				count += 1 
				p = p.next
			print("Size is ",count)
	
	def enqueue(self, data):
		temp = Node(data)
		if self.is_empty():
			self.front = self.rear = temp
		else:
			self.rear.next = temp 
			self.rear = temp
	
	def dequeue(self):
		if self.front is None:
			raise EmptyStackError("Stack is empty")
		elif self.front == self.rear:
			data = self.front.info
			self.front = self.rear = None
		else:
			data = self.front.info
			self.front = self.front.next
		return data
		
########################################

if __name__ == "__main__":
	#size = int(input("Enter the size of stack : "))
	s = QueueLinkedList()
	
	while True:
		print("#-------------Simple Stack with max_size Implementation-----------------#")
		print("1. Display")
		print("2. Enqueue")
		print("3. Dequeue")
		#print("4. Peek")
		print("5. Size")
		
		option = int(input("Enter your choice : "))
		
		if(option == 1):
			s.display()
		elif(option == 2):
			data = int(input("Enter the element to be pushed  : "))
			s.enqueue(data)
		elif(option == 3):
			data = s.dequeue()
			print("Popped data is ", data)
		elif(option == 4):
			#data = s.peek()
			print("Peeked data is ", data)
		elif(option == 5):
			s.size()
		else:
			print("Invalid option")