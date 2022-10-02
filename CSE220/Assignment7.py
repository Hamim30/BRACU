# Task 1

class keyindex:
    def __init__(self, a):
        i = 0
        minimum_value = a[0]
        # minimum value check
        while i < len(a):
            if a[i] < minimum_value:
                minimum_value = a[i]
            i += 1
        self.minimum = minimum_value  # used instance varible
        # if array have negative number
        if minimum_value < 0:
            i = 0
            while i < len(a):
                a[i] = (a[i] + (minimum_value * (-1)))
                i += 1
        # maximum value check

        maximum_value = a[0]
        i = 0
        while i < len(a):
            if a[i] > maximum_value:
                maximum_value = a[i]
            i += 1

        k = [0] * (maximum_value + 1)
        i = 0
        while i < len(a):
            k[a[i]] = 1
            i += 1
        self.k = k

    def search(self, key):
        if self.minimum < 0:
            key = key + (self.minimum * (-1))
        if key > len(self.k) - 1:
            return False
        if self.k[key] == 1:
            return True
        else:
            return False

    def sort(self):
        i = 0
        c = 0
        while i < len(self.k):
            if self.k[i] == 1:
                c += 1
            i += 1
        a = [0] * c
        i = 0
        j = 0
        while i < len(self.k):
            if self.k[i] == 1:
                if self.minimum < 0:
                    a[j] = i + (self.minimum)
                    j += 1
                else:
                    a[j] = i
                    j += 1
            i += 1
        return a


# tester
obj = keyindex([1, -5, 6, 8, -7, 9, 4])
print(obj.search(6))
print("SORTED: ", obj.sort())
obj2 = keyindex([-1, -5, -6, -8, -7, -9, -4])
print(obj2.search(-6))
print("SORTED: ", obj2.sort())
print(obj2.search(6))
print(obj.search(100))


# Task 2

def hashtable(array):
    hash_table = [0] * 9
    i = 0
    while i < len(array):
        value = 0
        j = 0
        cons = 0
        string = array[i]
        while j < len(string):
            if string[j] not in "AEIOU":
                cons += 1
            if ord(array[i][j]) >= 48 and ord(array[i][j]) <= 57:
                value += int(array[i][j])
            j += 1
        value += cons * 24
        i += 1
        mod = value % 9
        print(mod)
        if hash_table[mod] == 0:
            hash_table[mod] = string
        else:
            while hash_table[mod] != 0:
                mod += 1
                if mod == 9:
                    mod = 0
            hash_table[mod] = string
    return hash_table


print(hashtable(["ST1E89B8A32", "ST1E89B8A33", "ST1E89B8A42"]))