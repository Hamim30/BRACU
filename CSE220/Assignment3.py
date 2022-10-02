class Node:
    def __init__(self,element , next, previous):
        self.element=element
        self.next=next
        self.prev=previous
class DoublyList:
    def __init__(self ,array):
        self.head=Node(None, None,None)
        self.head.next=self.head
        self.head.prev=self.head
        for element in array:
            n=Node(element , None,None)
            if self.head.prev==self.head:
                n.next=self.head.next
                n.prev=self.head
                self.head.next=n
                self.head.prev=n
            else:
                tail = self.head.next
                while tail.next is not self.head:
                    tail = tail.next
                tail.next=n
                n.next=self.head
                n.prev=tail
                self.head.prev=n
    def showList(self):
        n = self.head.next
        if n==None:
            print("Empty List")
        else:
            print("Forward Printing: ",end="")
            while n is not self.head:
                print(n.element,end=" ")
                n = n.next
            print()
            #for backward iteration
#             print("Backward Printing: ",end="")
#             n = self.head.prev
#             while n is not self.head:
#                 print(n.element,end=" ")
#                 n = n.prev
#             print()
    def insert(self, newElement):
        n=Node(newElement,None,None)
        tail = self.head.next
        found=False
        while tail.next is not self.head:
            if newElement==tail.element:
                found=True
            tail = tail.next
        if tail.element==newElement:
            found=True
        if found:
            print("Already exist")
        else:
            tail.next=n
            n.next=self.head
            n.prev=tail
            self.head.prev=n
            print("Insertion Done")
    def nodeAT(self,index):
        n=self.head.next
        i=0
        while i!=index:
            n = n.next
            i+=1
        return n
    def counter(self):
        n=self.head.next
        i=0
        while n is not self.head:
            n = n.next
            i+=1
        return i
    def insert_index(self, newElement, index):
        n=self.head.next
        found=False
        while n is not self.head:
            if n.element==newElement:
                found=True
            n = n.next
        if found:
            print("Already exist")
        else:
            if index<0 or index>(self.counter())-1:
                print("invalid")
            elif index==0:
                n=Node(newElement,None,None)
                first_element=self.head.next
                n.prev=self.head
                self.head.next=n
                n.next=first_element
                first_element.prev=n
                print("Insertion Done")
            elif index==(self.counter()-1):
                present_element=self.nodeAT(index)
                n=Node(newElement,None,None)
                present_element.next=n
                n.prev=present_element
                n.next=self.head
                self.head.prev=n
                print("Insertion Done")
            else:
                previous_element=self.nodeAT(index-1)
                present_element=self.nodeAT(index)
                n=Node(newElement,None,None)
                previous_element.next=n
                present_element.prev=n
                n.next=present_element
                n.prev=previous_element
                print("Insertion Done")
    def remove(self, index):
        if index<0 or index>(self.counter()-1):
            print("Invalid")
        elif index==0:
            self.head.next=self.head.next.next
            self.head.next.prev=self.head
        elif index==(self.counter()-1):
            prev_tail=self.nodeAT(index-1)
            prev_tail.next=self.head
            self.head.prev=prev_tail
        else:
            remove_prev=self.nodeAT(index-1)
            remove_next=self.nodeAT(index+1)
            remove_prev.next=remove_next
            remove_next.prev=remove_prev
    def remove_element(self,deletekey):
        n=self.head.next
        i=0
        found=False
        while n is not self.head:
            if n.element==deletekey:
                found=True
                break
            n = n.next
            i+=1
        if found:
            self.remove(i)
            return deletekey
        else:
            print("Element is not available")
obj=DoublyList([1,2,3,0,5,6,7])
obj.showList()
obj.insert(12)
obj.showList()
obj.insert_index(7,6)
obj.showList()
print("Length: ",obj.counter())
obj.insert_index(10,4)
obj.showList()
obj.remove(6)
print("Deleted:",obj.remove_element(0))
obj.showList()