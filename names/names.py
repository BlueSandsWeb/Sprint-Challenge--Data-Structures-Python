import time

start_time = time.time()


# original
# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# mine

# Algo 1:
# O(n log(n) + n log(n)) => O(n log n):
# description: try making a binary search for each using names as numbers.
# steps:
    # create a binary list of the first names_1
    # binary search for names_2 in names_1
    # if it encounters one that is the same, add the name to a global array as a duplicate
    # return array and duplicates count is array length

class BinarySearchTree:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return "Done"
        current_node = self
        if value >= current_node.value:
            if current_node.right is not None:
                current_node.right.insert(value)
                # print("insert right")
            else:
                current_node.right = BinarySearchTree(value)
                return "Done"
        else:
            if current_node.left is not None:
                # print("insert left")
                current_node.left.insert(value)
            else:
                current_node.left = BinarySearchTree(value)
                return "Done"

    def contains(self, target):
        current_node = self
        if target+"\n" == current_node.value:
            return True
        if target >= current_node.value:
            if current_node.right is not None:
                return current_node.right.contains(target)
            else:
                return False
        else:
            if current_node.left is not None:
                return current_node.left.contains(target)
            else:
                return False

tree = BinarySearchTree()
f = open('names_1.txt', 'r')
for line in f:
    tree.insert(line)
f.close()

duplicates = []

# print(tree.contains("Jean Velazquez"))

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

for i in range(len(names_2)):
    if tree.contains(names_2[i]) == True:
        duplicates.append(names_2[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# Algo 2:
# O(n) ish
# import the first list of names as a list
# make one of the names a lookup table when it's imported by making it a set
# loop through all of the names from list one and look for them in list two
# if they're in there, store them into a third list named duplicates

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

duplicates = [ item for item in names_1 if item in names_2]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

