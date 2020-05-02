# Using one variable temp

def array_rotate(arr,d):
    length = len(arr)
    for i in range(d):
        leftShiftByOne(arr,length)

def leftShiftByOne(arr,length):
    temp = arr[0]
    for i in range(length-1):
        arr[i] = arr[i+1]
    arr[length - 1] = temp

# Utility  function
def _print(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

# Driver code
arr = [1,2,3,4,5,6,7,8,9]
_print(arr)
print(" ")
d = 3
print("Shift by ", d)
array_rotate(arr,d)
_print(arr)