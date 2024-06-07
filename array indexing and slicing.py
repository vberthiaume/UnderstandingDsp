import numpy as np

#clear the terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#numpy array slicing: https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
#prints elements 1 to 5 (so skipping element 0)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#print elements from index 4 to the end of the array:
print(arr[4:])

#print elements from the beginning to index 4 (not included):
print(arr[:4])

#print from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])

#with a step value of 2, print every other element from index 1 to index 5:
print(arr[1:5:2])

#Return every other element from the entire array:
print(arr[::2])

#2D array: From the second row, slice elements from index 1 to index 4 (not included):
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4])

#From both rows, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr2[0:2, 1:4])