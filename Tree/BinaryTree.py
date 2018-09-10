#BinaryTree.py
from collections import deque


class Node():
	def __init__(self, value):
		self.info = value
		self.lchild = None
		self.rchild = None

class BinaryTree():
	def __init__(self):
		self.root = None
		
	def create_tree(self):
		self.root = Node('P')
		self.root.lchild = Node('Q')
		self.root.rchild = Node('R')
		self.root.lchild.lchild = Node('A')
		self.root.lchild.rchild = Node('B')
		self.root.rchild.lchild = Node('X')
		
	def pre_order(self):
		self._pre_order(self.root)
		print()
		
	def _pre_order(self, p):
		if p is None:
			return 
		print(p.info, " ",end='')
		self._pre_order(p.lchild)
		self._pre_order(p.rchild)
		
	
	def in_order(self):
		self._in_order(self.root)
		print()
	
	def _in_order(self, p):
		if p is None:
			return 
		self._in_order(p.lchild)
		print(p.info, " ",end='')
		self._in_order(p.rchild)
		
	def post_order(self):
		self._post_order(self.root)
		print()
		
	def _post_order(self, p):
		if p is None:
			return 
		
		self._post_order(p.lchild)
		self._post_order(p.rchild)
		print(p.info, " ",end='')
		
	def level_order(self):
		if self.root is None:
			print("Tree is empty")
			return 
		dq = deque()
		dq.append(self.root)
		while len(dq) != 0:
			p = dq.popleft()
			print(p.info, " ", end='')
			if p.lchild is not None:
				dq.append(p.lchild)
			if p.rchild is not None:
				dq.append(p.rchild)
		print()
		
	def level_order1(self):
		if self.root is None:
			print("Tree is empty")
			return
		dq = deque()
		dq.append(self.root)
		self._level_order(dq)
		print()
		
	def _level_order(self, dq):
		if len(dq) == 0:
			return 
		p = dq.popleft()
		print(p.info, " ", end='')
		if p.lchild is not None:
			dq.append(p.lchild)
		if p.rchild is not None:
			dq.append(p.rchild)
		self._level_order(dq)
	
	def height(self):
		return self._height(self.root)
	
	def _height(self, p):
		if p is None:
			return 0
		hL = self._height(p.lchild)
		hR = self._height(p.rchild)
		
		if hL > hR:
			return 1 + hL
		else:
			return 1 + hR
			
	def search_it(self, x):
		p = self.root
		while p is not None:
			if x > p.info:
				p = p.rchild
			elif x < p.info:
				p = p.lchild
			else:
				return True
		return False
		
	def search_rec(self,x):
		#return self._search_rec(self.root,x) is not None
		return self._search_rec(self.root,x)
	
	def _search_rec(self, p, x):
		if p is None:
			return None
		if x > p.info:
			return self._search_rec(p.rchild,x)
		if x < p.info:
			return self._search_rec(p.lchild, x)
		return p
	
	def insert(self,data):		
		p = self.root 	
		par = None
		while p is not None:
			par = p 
			if data < p.info:
				p = p.lchild
			elif data > p.info :
				p = p.rchild
			else:
				print(data, " is present in the list")
				return 
				
		temp = Node(data)
		if par == None:
			self.root = temp
		elif data < par.info:
			par.lchild = temp
		else:
			par.rchild = temp
			
	def delete(self, data):
		p = self.root
		par = None 
		
		while p is not None: #finding the node to be deleted(p), par - p's parent
			if data == p.info:
				break 
			par = p
			if data < p.info:
				p = p.lchild 
			else:
				p = p.rchild
				
		if p == None:
			print(data, " is not present")
			return 
			
		#Case C: 2 children
		if p.lchild is not None and p.rchild is not None:
			ps = p 
			s = p.rchild 
			
			while s.lchild is not None:
				ps = s 
				s = s.lchild
			p.info = s.info 
			p = s 
			par = ps 
		
		#Case A or B:   
		if p.lchild is not None:
			ch = p.lchild
		else:
			ch = p.rchild
		
		if par == None:
			self.root = ch
		elif par.lchild == p:
			par.lchild = ch
		else:
			par.rchild = ch
			
		
	def delete_rec(self,x):
		self.root = self._delete_rec(self.root, x)
	
	def _delete_rec(self, p, x):
		if p is None:
			print(x, " is not found")
			return p
		
		if x < p.info:
			p.lchild = self._delete_rec(p.lchild,x)
		elif x > p.info:
			p.rchild = self._delete_rec(p.rchild,x)
		else:
			if p.lchild is not None and p.rchild is not None:
				s = p.rchild
				while s.lchild is not None:
					s = s.lchild
				p.info = s.info 
				p.rchild = self._delete_rec(p.rchild,s.info)
				
			else:
				if p.lchild is not None:
					ch = p.lchild 
				else:
					ch = p.rchild 
				p = ch
		return p 
		
	
###########################################################################################

bt = BinaryTree()
bt.create_tree()
print("Pre-Order")
bt.pre_order()
print("In-Order")
bt.in_order()
print("Post-Order")
bt.post_order()
print("Level order")
bt.level_order()
print("Height of the tree : ", bt.height()) 

x = (input("Enter element to be searched : "))
print(bt.search_it(x))

bt.root = None
num = int(input("Enter number of nodes to be inserted : "))
for i in range(num):
	data = int(input("Enter element to be inserted : "))
	bt.insert(data)

print("Level order")
bt.level_order()

data = int(input("Enter element to be deleted : "))
bt.delete_rec(data)

print("Level order")
bt.level_order()
