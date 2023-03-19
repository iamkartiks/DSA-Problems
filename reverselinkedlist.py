class Node():
    def __init__(self,data):
        self.data = data
        self.link = None

def reverse():
    
    a = Node(5)
    b = Node(4)
    c = Node(7)
    d = Node(0)

    a.link = b
    b.link = c
    c.link = d

    temp = a
    while temp!= None:
        print(temp.data,'->',end=" ")
        temp = temp.link

    
    prev = None
    current = a

    while current !=None:
        link = current.link
        current.next = prev
        prev = current
        current = link
    a = prev

    temp = a
    while temp!= None:
        print("\nREVERSE")
        print(temp.data,'->',end=" ")
        temp = temp.link



reverse()