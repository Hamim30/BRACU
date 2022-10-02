#Task 1
(a)
def factorial(n):
    if n== 0 or n==1:
        return n
    else:
        return n*factorial(n-1)
n=int(input("Factorial :"))
print(factorial(n))

(b)
def fibonacci(n):
    if n==0 or n==1:
        return n
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
user_input=int(input())
for i in range (0,user_input):
    print(i+1,"th fibonacci number is: ",fibonacci(i))

(c)
array=[1,2,3,4,5,6,7,8]
def print_array(array):
    if len(array)==0:
        return
    print(array[0])
    print_array(array[1:])
print_array(array)
(d)
def powerN(number, power):
    if power==0:
        return 1
    elif number==0:
        return 0
    else:
        return number *powerN(number, power-1)
print(powerN(10,3))

#Task 2
(a)
def deciman_to_binary(binary,decimal_number):
    if decimal_number==1:
        return "1"+binary
    else:
        binary=str(decimal_number%2)+binary
        return deciman_to_binary(binary,decimal_number//2)
number=int(input("Decimal: " ))
print("Binary: ",deciman_to_binary("",number))

(b)
class Node:
    def __init__(self, element , next):
        self. element =element
        self.next=next
class LinkedList:
    def __init__(self, array):
        self.head=None
        self.tail=None
        self.sum_element=0
        for digit in array:
            n=Node(digit, None)
            if self.head==None:
                self.head=n
                self.head.next=self.head
                self.tail=self.head
            else:
                self.tail.next=n
                n.next=self.head
                self.tail=n
    def sum_all_element(self,head):
        if self.tail==head:
            return self.sum_element+self.tail.element
        self.sum_element+=head.element
        return self.sum_all_element(head.next)#recursive algorithm
obj=LinkedList([1,2,3,4,6,5,10])
print(obj.sum_all_element(obj.head))

(c)
class Node:
    def __init__(self, element , next):
        self. element =element
        self.next=next
class LinkedList:
    def __init__(self, array):
        self.head=None
        self.tail=None
        self.sum_element=0
        for digit in array:
            n=Node(digit, None)
            if self.head==None:
                self.head=n
                self.head.next=self.head
                self.tail=self.head
            else:
                self.tail.next=n
                n.next=self.head
                self.tail=n
    def reverse_order(self,head):
        if head==self.tail:
            return str(self.tail.element)
        else:
            return self.reverse_order(head.next)+" "+str(head.element)
obj=LinkedList([1,2,3,4,6,5,7])
print(obj.reverse_order(obj.head))

(3)
def hocBuilder(height):
    if height==0:
        return 0
    elif height==1:
        return 8
    else:
        return hocBuilder(height-1)+5
user_input=int(input("Height: "))
print("cards required ",hocBuilder(user_input))

(4)
(a)
def Pattern(column,counter):
    if counter==1:
        return "1"
    elif column==1:
        return Pattern(counter-1,counter-1)+'\n'+"1"
    else:
        return Pattern(column-1,counter)+str(column)
user_input=int(input("Enter a number:"))
print(Pattern(user_input,user_input))

(b)
def Pattern(column,counter,base):
    if counter==1:
        return (" "*(base-1))+"1"
    elif column==1:
        return Pattern(counter-1,counter-1,base)+'\n'+(" "*(base-counter))+"1"
    else:
        return Pattern(column-1,counter,base)+str(column)
user_input=int(input("Enter a number:"))
print(Pattern(user_input,user_input,user_input))

(c)
class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            print("For invextement of",array[idx],"Profit will be:", profit)
            self.print(array,idx+1)
        else:
            return 0
    def calcProfit(self,investment):
        if investment==25000:
            return 0
        elif investment>25000 and investment<=100000:
            return self.calcProfit(investment-1000)+45
        elif  investment>100000:
            return self.calcProfit(investment-1000)+80
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)