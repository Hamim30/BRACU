##Task 1
def shiftLeft(source, k):
    index = 0
    while (index + k) < len(source):
        source[index] = source[index + k]
        index += 1
    index = len(source) - 1
    counter = 0
    while counter < k:
        source[index] = 0
        index -= 1
        counter += 1
    print(source)


source = [10, 20, 30, 40, 50, 60]
k = int(input("Enter the shifting position:"))
shiftLeft(source, k)


##Task 2
def rotateLeft(source, k):
    k = k % len(source)
    temp_array = [0] * k
    index = 0
    while index < k:
        temp_array[index] = source[index]
        index += 1
    index = 0
    while (index + k) < len(source):
        source[index] = source[index + k]
        index += 1

    index = len(source) - 1
    counter = len(temp_array) - 1
    while counter != -1:
        source[index] = temp_array[counter]
        index -= 1
        counter -= 1
    print(source)


source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 13)


##Task 3

def remove(source, size, remove_index):
    source[remove_index] = 0
    index = size
    while remove_index < index:
        source[remove_index] = source[remove_index + 1]
        remove_index += 1
    print(source)


source = [10, 20, 30, 40, 40, 80, 50, 0, 0]
remove(source, 7, 6)


##Task 4
def removeAll(source, size, element):
    index = 0
    afterRM_size = size  # to control the second loop
    while index < size:
        if source[index] == element:
            source[index] = 0
            afterRM_size -= 1
        index += 1
    temp = [0] * len(source)
    index = 0
    i = 0
    while i < afterRM_size:
        if source[index] != 0:
            temp[i] = source[index]
            i += 1
        index += 1
    print(temp)


source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 10)


##Task 5
def splittingArray(source):
    pointer = 0
    pointer_one = 1
    pointer_two = len(source) - 1
    flag = False
    while pointer_one < pointer_two:
        sum_one = 0
        index = 0
        while index <= pointer_one:
            sum_one += source[index]
            index += 1
        sum_two = 0
        index = pointer_one + 1
        while index <= pointer_two:
            sum_two += source[index]
            index += 1
        if sum_one == sum_two:
            flag = True
            break
        pointer_one += 1
    if flag:
        print("true")
    else:
        print("false")


source = [10, 4, 1, 1, 2, 10]
splittingArray(source)


##Task 6
def arraySeries(n):
    array = [0] * (n * n)
    index = 1
    while (index <= n):
        value = 1
        value_index = (n * index) - 1  # 2,5,8
        while (value <= index):  # divide by group of n
            array[value_index] = value
            value += 1
            value_index -= 1
        index += 1
    return array


output = arraySeries(int(input()))
print(output)


##Task 7
def bunch(source):
    most_bunch = 0
    index = 0
    while index < len(source):
        check = source[index]
        pointer_one = 0
        pointer_two = len(source)
        bunch_counter = 1
        while pointer_one < pointer_two:
            if source[pointer_one] == check:
                bunch_counter += 1
            pointer_one += 1
        if most_bunch < bunch_counter:
            most_bunch = bunch_counter
        index += 1
    return (most_bunch)


result = bunch([1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4])
print(result)


## Task 8

def repitation(source):
    index = 0
    unique_list = [0] * len(source)
    repitation_counter = [0] * len(source)
    while index < len(source):
        check = source[index]
        pointer_one = 0
        counter = 0
        while pointer_one < len(source):
            if source[pointer_one] == check:
                counter += 1
                pointer_one += 1
            else:
                pointer_one += 1
        flag = False
        i = 0
        while i < len(source):
            if unique_list[i] == check:
                flag = True
                break
            i += 1
        index += 1
        if flag:
            continue
        else:
            unique_list[index - 1] = check
            if counter > 1:
                repitation_counter[index - 1] = counter
            else:
                repitation_counter[index - 1] = 0

    ##check repitation array same time of repitation or not
    index_of_check = 0
    flag = False
    while index_of_check < len(repitation_counter):
        checker = repitation_counter[index_of_check]
        index_of_match = 0
        counter = 0
        index_of_check += 1
        while index_of_match < len(repitation_counter):
            if repitation_counter[index_of_match] == checker and checker != 0:
                counter += 1
            index_of_match += 1
        if counter > 1:
            flag = True
            break
    if flag:
        return ("true")
    else:
        return ("false")


result = repitation([3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6])
print(result)


##Circular
##task 1
def palindrome(source, start, size):
    temp_array = [0] * size
    index = start
    i = 0

    # converting circular to linear
    while i < size:
        temp_array[i] = source[index]
        index = (index + 1) % len(source)
        i += 1
    pointer_one = 0
    pointer_two = size - 1
    checker = False

    # palindrome checking by pointer
    while pointer_one < pointer_two:
        if temp_array[pointer_one] == temp_array[pointer_two]:
            checker = True
        else:
            checker = False
            break
        pointer_one += 1
        pointer_two -= 1
    if checker:
        return ("true")
    else:
        return ("false")


print(palindrome([20, 10, 0, 0, 0, 10, 20, 30], 5, 5))


##Task2

def linearConverter(source_one, source_one_start, source_one_size, source_two, source_two_start, source_two_size):
    if len(source_one) > len(source_two):
        temp = [0] * len(source_one)
    else:
        temp = [0] * len(source_two)
    index = 0
    element_counter = 0
    common_key_index = 0
    while index < source_one_size:
        check = source_one[source_one_start]
        source_one_start = (source_one_start + 1) % len(source_one)
        counter = 0
        while counter < source_two_size:
            if check == source_two[source_two_start]:
                temp[common_key_index] = check
                common_key_index += 1
                element_counter += 1
                break
            source_two_start = (source_two_start + 1) % len(source_two)
            counter += 1
        index += 1
    linear_array = [0] * element_counter
    index = 0
    while index < element_counter:
        linear_array[index] = temp[index]
        index += 1

    # if the final output also have common element
    temp_array = [0] * len(linear_array)
    idx = 0
    c = 0
    while idx < len(linear_array):
        check = linear_array[idx]
        idx2 = 0
        present = False
        idx += 1
        while idx2 < len(temp_array):
            if check == temp_array[idx2]:
                present = True
                break
            idx2 += 1
        if present:
            continue
        else:
            temp_array[c] = linear_array[idx - 1]
            c += 1
    output = [0] * c
    index = 0
    while index < c:
        output[index] = temp_array[index]
        index += 1
    return output


output = linearConverter([40, 40, 5, 0, 0, 10, 20, 30], 5, 6, [10, 20, 21, 0, 0, 0, 0, 0, 5, 40, 15, 25], 8, 7)
print(output)

##Task 3

import random


def musicalChair(source):
    index = 0
    ran = 0
    while ran != 1:
        ran = random.randint(0, 3)
        if ran == 1:
            index = len(source) // 2
            temp = [0] * (len(source) - 1)
        else:
            temp = source[len(source) - 1]
            index = len(source) - 1
            pointer = 0
            while (index > pointer):
                source[index] = source[index - 1]
                index -= 1
            source[0] = temp
        print("Rotate", source)
    pointer_one = 0
    idx = 0
    while pointer_one < len(source):

        if pointer_one != index:
            temp[idx] = source[pointer_one]
            idx += 1
        pointer_one += 1
    print("Someone Eliminated")
    print("Remaining Players:", temp)
    if len(temp) == 1:
        print("\nWinner Winner chicken Dinner\n")
        print(temp[0])
    else:
        musicalChair(temp)


musicalChair(["Hamim", "Arfan", "Miftah", "Asif", "Evan", "Jahur", "Taskin"])