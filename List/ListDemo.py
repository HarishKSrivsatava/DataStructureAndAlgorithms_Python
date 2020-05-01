list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# access element
print(list1[0])
print(list3[3])
print(list1[:]) # ['physics', 'chemistry', 1997, 2000]
print(list1[1:5]) # ['chemistry', 1997, 2000]
print(list1[1:]) # ['chemistry', 1997, 2000]
print(list1[:2]) # ['physics', 'chemistry']
print(list1[:-1]) # except last element ['physics', 'chemistry', 1997]
print(list1[-1:])# last element [2000]

# updation
list1[0] = 'xyz'
for i in list1:
    print(i , end = " ")
print("\n")
print(list1[:])


# Deletion
print(list1[:], end = " ") #['xyz', 'chemistry', 1997, 2000]
print("\n")
del list1[0] # delete element at index 0
print(list1[:], end = " ") #['chemistry', 1997, 2000]
