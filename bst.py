class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class bst:
	def __init__(self):
		self.root=None
	def append(self,data):
		if self.root==None:
			self.root=node(data)
		else:
			self._insert(data,self.root)
	def _insert(self,data,current):
		if data>current.data:
			if current.left!=None:
				current.left=node(data)
			else:
				self._insert(data,current.left)				
		elif data<current.data:
			if current.right!=None:
				current.right=node(data)
			else:
				 self._insert(data,current.right)	
		else:
			print("duplicate value")
	def show(self):
		self._show(self.root)
	def _show(self,curr):
		if curr:
			print(curr.data)
			self._show(curr.left)
			self._show(curr.right)
l1=bst()
l1.show()													
