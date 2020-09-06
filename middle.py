'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        
    def inserts(self):
        tmp=self.head
        n=int(input())
        for i in range(n):
            x=int(input())
            newnode=node(x)
            if self.head==None:
                head=newnode
            else:
                while tmp:
                    tmp=tmp.next
                tmp=newnode    
    def show(self):
        tmp=self.head
        while tmp:
            tmp=tmp.next
            print(tmp.data)
    def middles(self):
        slow=self.head
        fast=self.head
        while (fast.next!=None) and (fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
        print(slow.data)    
s1=linkedlist()
s1.inserts()
s1.middles()
