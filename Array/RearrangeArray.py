"""Given an array of elements of length N, ranging from 0 to N – 1.
All elements may not be present in the array. If element is not present then there will be -1 present
in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place."""

"""Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
         11, 12, 13, 14, 15, 16, 17, 18, 19]"""

"""Approach:
1. Navigate the array.
2. Check if a[i] = -1, if yes then ignore it.
3. If a[i] != -1, Check if element a[i] is at its cor­rect posi­tion (i=A[i]). If yes then ignore it.
4. If a[i] != -1 and ele­ment a[i] is not at its cor­rect posi­tion (i!=A[i]) then place it to its correct posi­tion, 
but there are two conditions:

Either A[i] is vacate, means A[i] = -1, then just put A[i] = i .
OR A[i] is not vacate, means A[i] = x, then int y=x put A[i] = i. Now, we need to place y to its 
correct place, so repeat from step 3."""

def fix(arr, len):
    for i in range(0,len):
        if(A[i] != -1 and A[i] != i):
            x = A[i]
            # check this location in the array is not vacate
            while(A[x] != -1 and A[x] != x): # this location niether not -1 nor having the correct value
               y = A[x]
               A[x] = x
               x = y
            A[x] = x
        # check if while loop has not set correct value at A[i]
        if(A[i] != i):
            A[i] = -1

def _print(arr):
    for i in range(len(arr)):
        print(arr[i] , end = " ")
# Driver code
A = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
_print(A)
print(" ")
fix(A, len(A))
_print(A)

""" Time complexity = O(n)
    Space complextity = O(1) """