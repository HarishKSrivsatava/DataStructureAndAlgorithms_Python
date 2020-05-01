from array import *
myArr = array('i',[10,20,30])
for i in range(len(myArr)):
   print(myArr[i], end =" ")
print("\n")
# insertion : insert at the index
myArr.insert(1,90)
for i in myArr:
    print(i,end = " ")
print("\n")
# insertion : insert at the end
myArr.append(100)
for i in myArr:
    print(i, end = " ")
print("\n")
# deletion
myArr.remove(10)
print("\n")
for i in myArr:
    print(i,end = " ")
print("\n")
# search
print(myArr.index(100))
# Updation
myArr[0] = 101
for i in myArr:
    print(i, end = " ")
