##Task 1
user_input = input()


class stack_array:
    def __init__(self):
        self.brackets = []
        self.pointer = -1
        self.size = self.pointer + 1
        self.brackets_index = []

    def push(self, bracket):
        self.brackets += [bracket]
        self.pointer += 1

    def pop(self):
        self.brackets = self.brackets[:self.pointer - 1]
        self.pointer -= 1
        self.brackets_index = self.brackets_index[:self.pointer - 1]

    def peek(self):
        return self.brackets[self.pointer]

    def empty_or_not(self):
        if self.pointer == -1:
            return True
        else:
            return False


stack = stack_array()
flag = True


def checker(flag):
    check = stack.peek()
    if (check == "(" and element == ")") or (check == "{" and element == "}") or (check == "[" and element == "]"):
        stack.pop()
        return True
    else:
        return False


message = ""
starter = True  # just to see where should we stop pushing
index = 0
for element in user_input:
    index += 1
    if element in "({[":
        stack.push(element)
        stack.brackets_index += [index]
    elif element in ")}]" and stack.empty_or_not():
        message = "Error at character # " + str(index) + ". ‘" + element + "‘- not opened."
        flag = False
        break
    elif element in ")}]":
        flag = checker(flag)
        if not flag:
            break

# expression is correct or not
if flag:
    print("This expression is correct")
else:
    print("This expression is not correct")
# if any error
if message == "" and not stack.empty_or_not():
    print("Error at character # ", stack.brackets_index[stack.pointer], ". ", stack.peek(), "- not closed.")
else:
    print(message)

##"==========================================================================================================================="
##Task 2

user_input = input()


class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class stack_linked_list:
    def __init__(self):
        self.head = None
        self.pointer = -1
        self.head_index = None

    def push(self, bracket, index):
        ref = Node(bracket, None)
        if self.head == None:
            self.head = ref
        else:
            self.head.next = self.head
            self.head = ref
        self.pointer += 1
        index = Node(index, None)
        if self.head_index == None:
            self.head_index = index
        else:
            self.head_index.next = self.head_index
            self.head_index = index

    def pop(self):
        self.head = self.head.next
        self.head_index = self.head_index.next
        self.pointer -= 1

    def peek(self):
        return self.head.element

    def empty_or_not(self):
        if self.pointer == -1:
            return True
        else:
            return False


stack = stack_linked_list()
flag = True


def checker(flag):
    check = stack.peek()
    if (check == "(" and element == ")") or (check == "{" and element == "}") or (check == "[" and element == "]"):
        stack.pop()
        return True
    else:
        return False


message = ""
starter = True  # just to see where should we stop pushing
index = 0
for element in user_input:
    index += 1
    if element in "({[":
        stack.push(element, index)
    elif element in ")}]" and stack.empty_or_not():
        message = "Error at character # " + str(index) + ". ‘" + element + "‘- not opened."
        flag = False
        break
    elif element in ")}]":
        flag = checker(flag)
        if not flag:
            break

# expression is correct or not
if flag:
    print("This expression is correct")
else:
    print("This expression is not correct")
# if any error
if message == "" and not stack.empty_or_not():
    print("Error at character # ", stack.head_index.element, ". ", stack.peek(), "- not closed.")
else:
    print(message)