'''
1- create node
2- create linked list
3- add nodes to linked list
4- print linked list
--------------------------
- create head point to null
- create node then 
'''
class Node:
    def __init__(self ,data=None, next=None) :
        self.data=data
        self.next=next
        
        

class LinkedList:
    def __init__(self) :
        self.head = None
        
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
        print(self.head) #<__main__.Node object at 0x7faa2f2738e0>
    
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        current_node = self.head
        llstr = ''
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
        

        


if __name__ == '__main__':
    ll=LinkedList()
    ll.print()
    ll.insert_at_begining(5)
    ll.insert_at_begining(50)
    ll.insert_at_begining(90)
    ll.print()