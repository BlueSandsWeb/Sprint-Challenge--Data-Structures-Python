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
# O(n log n):
# description: try making a binary search for each using names as numbers.
# steps:
    # create a binary list of the first names_1
    # binary search for names_2 in names_1
    # if it encounters one that is the same, add the name to a global array as a duplicate
    # return array and duplicates count is array length


# Algo 2:
# O(n) ish
# import the first list of names as a list
# make one of the names a lookup table when it's imported by making it a set
# loop through all of the names from list one and look for them in list two
# if they're in there, store them into a third list named duplicates

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

