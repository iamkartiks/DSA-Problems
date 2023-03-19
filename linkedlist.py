class Node():
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList():

    def __init__(self):
        self.head = None
    
    def insertbeginning(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node    
    
    def insertmiddle(self,data,pos):
        new_node = Node(data)
        c = 1
        temp = self.head
        while c<pos-1:
            # print(temp.data)
            c += 1
            temp = temp.next
        # print(temp.data)
        new_node.next = temp.next
        temp.next = new_node
    
    def traverse(self):
        temp = self.head
        while temp!= None:
            print(temp.data,'->',end="")
            temp = temp.next


    def reverse(self):
        prev = None
        current = self.head
        while current!=None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


ll = LinkedList()
ll.insertbeginning(1)
ll.insertbeginning(3)
ll.insertbeginning(2)
ll.insertmiddle(4,2)
print("before reversal")
ll.traverse()
ll.reverse()
print("after reversal")
ll.traverse()