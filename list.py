class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=node()
	def append(self):
		n=int(input("enter no."))
		data=[]
		for i in range(n):
			data=int(input())
		for i in range(n):	
		    newnode=node(data[i])
		    current=self.head
		    while(current.next!=None):
			     current=current.next
		    current.next=newnode
	def display(self):
		ele=[]
		curr=self.head
		while curr.next!=None:
			curr=curr.next
			ele.append(curr.data)
		print(ele)
l1=linkedlist()
l1.append()
l1.display()
								
