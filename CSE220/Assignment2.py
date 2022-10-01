class Node:
    def __init__(self, element , next):
        self.element=element
        self.next=next
class MyList:
    def __init__(self,a):
        self.head=None
        tail=None
        head=None
        for elements in a:
            ref=Node(elements,None)
            if self.head==None:
                self.head=ref
                tail=ref
            else:
                tail.next=ref
                tail=ref
    def showList(self):
        ref=self.head
        if ref==None:
            print("Empty list")
        else:
            while ref is not None:
                print(ref.element,end=" ")
                ref=ref.next
        print()
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    def clear(self):
        self.head=None
    def insert(self, newElement):
        ref=self.head
        checker=False
        while ref is not None:
            if ref.element==newElement:
                checker=True
                break
            else:
                ref=ref.next
        if checker:
            print("the key already exists and does not insert the key")
        else:
            ref=self.head
            while ref.next is not None:
                ref=ref.next
            ref.element=newElement
    def insert_index(self, newElement,index):
        if self.counter()<index or index<0:
            print("Invalid index")
        else:
            ref=self.head
            checker=False
            while ref is not None:
                if ref.element==newElement:
                    checker=True
                    break
                else:
                    ref=ref.next
            if checker:
                print("the key already exists and does not insert the key")
            else:
                i=0
                ref=self.head
                while ref.next is not None:
                    if i==index:
                        ref.element=newElement
                    i+=1
                    ref=ref.next
    def nodeAT(self,index):
        ref=self.head
        i=0
        while ref is not None:
            if i==index:
                return ref
            else:
                ref=ref.next
            i+=1
    def remove(self, deletekey):
        if (self.counter()-1)<deletekey or deletekey <0:
            return ("invalid")
        else:
            previous_ref=self.nodeAT(deletekey-1)
            delet_ref=self.nodeAT(deletekey)
            previous_ref.next=delet_ref.next
            return delet_ref.element
    def evenNumber(self):
        ref=self.head
        counter=0
        while ref is not None:
            if ref.element%2==0:
                counter+=1
            ref=ref.next
        ref=self.head
        even_list=[0]*counter
        i=0
        while ref is not None:
            if ref.element%2==0:
                even_list[i]=ref.element
                i+=1
            ref=ref.next
        return even_list
    def findElement(self,element):
        ref=self.head
        while ref is not None:
            if ref.element==element:
                return True
            ref=ref.next
        return False
    def sumElement(self):
        ref=self.head
        sum_e=0
        while ref is not None:
            sum_e+= ref.element
            ref=ref.next
        print(sum_e)
    #same as bux
    def reverseList1(self):
        New_head = None
        ref = self.head
        while ref is not None:
            next_Node = ref.next
            ref.next = New_head
            New_head = ref
            ref = next_Node
        self.head=New_head
    def counter(self):
        count=0
        ref=self.head
        while ref is not None:
            count+=1
            ref=ref.next
        self.count=count
        return count
    def sortList(self):
        ref=self.head
        length=self.counter()
        #to get tail
        while ref is not None:
            tail=ref
            ref=ref.next
        for i in range(0,length):
            ref_temp=self.head
            while ref_temp is not None:
                if ref_temp is not tail:
                    if ref_temp.element<ref_temp.next.element:
                        temp=ref_temp.element
                        ref_temp.element=ref_temp.next.element
                        ref_temp.next.element=temp
                ref_temp=ref_temp.next
    def rotateLeft(self):
        newhead=self.nodeAT(1)
        prevhead=self.head
        tail=self.nodeAT(self.counter()-1)
        tail.next=prevhead
        prevhead.next=None
        self.head=newhead
obj=MyList([1,2,3,4,12,6,15,8,9,10])
#obj.showList()
# obj.reverseList1()
# obj.showList()
# obj.sumElement()
# obj.showList()
# print(obj.findElement(2))
# obj.showList()
# print(obj.evenNumber())
# obj.showList()
# print(obj.remove(10))
# obj.showList()
# obj.insert_index(33,2)
# obj.showList()
# obj.insert(14)
# obj.showList()
# obj.clear()
# obj.showList()
# print(obj.isEmpty())
# obj.showList()
# obj.sortList()
# obj.showList()
# obj.rotateLeft()
# obj.showList()
# obj.rotateLeft()
# obj.showList()
# obj.rotateLeft()
# obj.showList()