##Task 1

def selection_sort(array, index, next, length):
    if next == length:
        return
    if index < length - 1:
        min = index
        while next < length:
            if array[next] < array[min]:
                min = next
            next = next + 1
        if min != index:
            temp = array[index]
            array[index] = array[min]
            array[min] = temp
        selection_sort(array, index + 1, index + 2, length)


A = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
# A=[22,5,14,2,7,1]
i = 0
j = 1
sorted_array = selection_sort(A, i, j, len(A))
print(A)


# Task2

def insertion_sort(array, index, length):
    if index == length:
        return -1
    if index < length:
        j = index - 1
        insert_value = array[index]
        # shifting till get the right position
        while j >= 0 and insert_value < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = insert_value
        insertion_sort(array, index + 1, length)


A = [22, 5, 14, 2, 7, 1]
i = 1
insertion_sort(A, i, len(A))
print(A)


# task3

class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
    def __init__(self, array):
        self.head = None
        tail = None
        for element in array:
            ref = Node(element, None)
            if self.head == None:
                self.head = ref
                tail = ref
            else:
                tail.next = ref
                tail = ref

    def counter(self):
        ref = self.head
        counter = 0
        while ref is not None:
            counter += 1
            ref = ref.next
        return counter

    def bubble_sort(self, i, head, length):
        if i == length - 1:
            self.head = head
            return
        ref = head
        ref2 = head.next
        while ref2 is not None:
            if ref.element < ref2.element:
                temp = ref.element
                ref.element = ref2.element
                ref2.element = temp
            ref = ref2
            ref2 = ref2.next
        self.bubble_sort(i + 1, self.head, length)

    def print_array(self):
        ref = self.head
        while ref is not None:
            print(ref.element)
            ref = ref.next


A = [22, 5, 14, 2, 7, 1]
obj = LinkedList(A)
obj.bubble_sort(0, obj.head, obj.counter())
obj.print_array()


# Task 4

class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
    def __init__(self, array):
        self.head = None
        tail = None
        for element in array:
            ref = Node(element, None)
            if self.head == None:
                self.head = ref
                tail = ref
            else:
                tail.next = ref
                tail = ref

    def counter(self):
        ref = self.head
        counter = 0
        while ref is not None:
            counter += 1
            ref = ref.next
        return counter

    def selection_sort(self, next, length, min):
        if next < length:
            ref = min.next
            key = min
            while ref is not None:
                if ref.element < min.element:
                    min = ref
                ref = ref.next
            if min != key:
                temp = min.element
                min.element = key.element
                key.element = temp
            self.selection_sort(next + 1, length, key.next)
        else:
            return

    def print_array(self):
        ref = self.head
        while ref is not None:
            print(ref.element)
            ref = ref.next


A = [22, 5, 14, 2, 7, 1]
obj = LinkedList(A)
obj.selection_sort(0, obj.counter(), obj.head)
obj.print_array()


# Task 5

class Node:
    def __init__(self, element, next, prev):
        self.element = element
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, array):
        self.head = None
        self.tail = None
        for element in array:
            ref = Node(element, None, None)
            if self.head == None:
                self.head = ref
                self.tail = ref
            else:
                self.tail.next = ref
                ref.prev = self.tail
                self.tail = ref

    def print_a(self):
        ref = self.head.next
        while ref.next is not None:
            print(ref.element, end=" ")
            ref = ref.next
        print(ref.element)

    def print_e(self):
        ref = self.tail
        while ref.prev is not None:
            print(ref.element, end=" ")
            ref = ref.prev
        print(ref.element)

    def insertion_sort(self, ref):
        if ref == None:
            return
        else:
            min = ref
            comp = ref.element
            while min.prev is not None and min.prev.element > comp:
                min.element = min.prev.element
                min = min.prev
            if min.element != comp:
                min.element = comp
            self.insertion_sort(ref.next)


A = [1, 100, 2, 200, 3, 300, 42, 53]
obj = LinkedList(A)
obj.insertion_sort(obj.head)
print("Forward order:")
obj.print_a()
print("Reverse order:")
obj.print_e()


# Task 6
def binary_search(array, search, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if search == array[mid]:
            return mid
        elif search > array[mid]:
            return binary_search(array, search, mid + 1, right)
        else:
            return binary_search(array, search, left, mid - 1)


array = [1, 2, 3, 4, 5, 6, 7, 8]
left = 0
right = len(array) - 1
user_input = int(input())
a = binary_search(array, user_input, left, right)
if a == -1:
    print("There is no such an element")
else:
    print("Index of", user_input, "in array is:", a)


# task 7

def fibonacci(nth_fibonacci, array):
    if array[nth_fibonacci] > 0:
        return array[nth_fibonacci]
    if nth_fibonacci == 0 or nth_fibonacci == 1 or nth_fibonacci == 2:
        if nth_fibonacci == 2:
            array[nth_fibonacci] = 1
        else:
            array[nth_fibonacci] = nth_fibonacci
        return array[nth_fibonacci]
    else:
        array[nth_fibonacci] = fibonacci(nth_fibonacci - 1, array) + fibonacci(nth_fibonacci - 2, array)
        return array[nth_fibonacci]


user_input = int(input())
array = [0] * (user_input + 1)
print(user_input, "th Fibonacci number is:", fibonacci(user_input, array))