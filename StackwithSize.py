# Stackwithlength.py	
#  Stack implementaiotn with defining the size of stack.

class EmptyStackError(Exception):
	pass

class StackFullError(Exception):
	pass
	
class StackwithSize:
	def __init__(self, max_size):
		self.stack = [None] * max_size
		self.count = 0
		
		
	def is_empty(self):
		return self.count==0
		
	def is_full(self):
		return self.count==len(self.stack)
		
	def push(self, data):
		if self.count == len(self.stack):
			raise StackFullError("Stack is full")
			
		self.stack[self.count] = data
		self.count += 1		
	
	def pop(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		
		self.count -= 1
		data = self.stack[self.count]
		self.stack[self.count] = None
		return data
		
	def peek(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		
		self.count -= 1
		data = self.stack[self.count]
		return data
		
	def display(self):
		print(self.stack)
	'''
		for i in range(len(self.stack)):
			print(self.stack[i], " " , end='')
		print()
	'''	
##################################################

if __name__ == "__main__":
	size = int(input("Enter the size of stack : "))
	s = StackwithSize(size)
	
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