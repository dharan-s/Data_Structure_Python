#Paracheck.py -- Paranthesis check in an expression

from Stack import Stack

def is_valid(expr):
	st = Stack()
	
	for ch in expr:
	
		if ch in '({[':
			st.push(ch)
			
		if ch in '}])':
			if st.is_empty():
				print("Right paranthesis is more")
				return False 
			else:
				left = st.pop()
				if not match_paranthesis(left, ch):
					print("Paranthesis mismatch")
					return False
				
	if st.is_empty():
		return True
	else:
		print("Left paranthesis is more ")
		return False 
				
def match_paranthesis(left_para,right_para):
	if left_para == '(' and right_para == ')':
		return True
	if left_para == '{' and right_para == '}':
		return True
	if left_para == '[' and right_para == ']':
		return True
	return False
	
###################

while True:
	print("Enter an expression with paranthesis (q=Quit) : ", end = ' ')
	expression = input()
	
	if expression == 'q':
		break 
		
	if is_valid(expression):
		print("Valid Expression")
	else:
		print("Invalid Expression")