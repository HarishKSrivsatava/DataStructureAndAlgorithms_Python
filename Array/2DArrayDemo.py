from array import *

# Access the elements
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0]) #[11, 12, 5, 2]
print(T[0][0]) #11
print(T[1][1]) #6

# print all the elements of 2D array
for i in T:
    for x in i:
        print(x, end = " ")
    print(" ")
# Insertion
T.insert(0,[2,7,9,78,6])
for i in T:
    for x in i:
        print(x, end = " ")
    print(" ")

T1 = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
for i in T1:
    for x in i :
        print(x, end = " ")
    print(" ")
T1[0,0] = 99 # Update one element at index (0,0)
for i in T1:
    for x in i :
        print(x, end = " ")
    print(" ")