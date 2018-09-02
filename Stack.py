# Stack.py	

class EmptyStackError(Exception):
	pass

class Stack:
	def __init__(self):
		self.stack = []
		
	def is_empty(self):
		return self.stack==[]
	
	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		return self.stack.pop()
		
	def peek(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		return self.stack[-1]
		
	def display(self):
		print(self.stack)
	'''
		for i in range(len(self.stack)):
			print(self.stack[i], " " , end='')
		print()
	'''	
##################################################

if __name__ == "__main__":
	s = Stack()
	
	while True:
		print("#-------------Simple Stack Implementation-----------------#")
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
			#s.pop()
			data = s.pop()
			print("Popped data is ", data)
		elif(option == 4):
			data = s.peek()
			print("Peeked data is ", data)
		elif(option == 5):
			break
		else:
			print("Invalid option")