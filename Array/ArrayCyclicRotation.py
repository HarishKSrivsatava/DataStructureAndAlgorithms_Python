def _cyclic_rotation(arr):
    n = len(arr)
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
    arr[0] = x;

def _print(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")

#Driver Code
arr = [1,2,3,4,5,6]
_print(arr)
print(" ")
_cyclic_rotation(arr)
_print(arr)
