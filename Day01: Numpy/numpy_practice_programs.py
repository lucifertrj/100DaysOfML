"""
1.Create a Matrix whose border are 1 and the inside content is 0.

Sample Input:

[[1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1.]]

Sample Output:
[[1., 1., 1., 1., 1.],
 [1., 0., 0., 0., 1.],
 [1., 0., 0., 0., 1.],
 [1., 0., 0., 0., 1.],
 [1., 1., 1., 1., 1.]]
"""
import numpy as np
arr = np.ones((5,5))
arr[1:-1,1:-1] = 0
print(arr)
"""
2. Create a (mxn)square matrix with range of 1 to n*n. And update its border to 0.

We know that: m=n since it is square matrix.

Sample Input 1: (3x3) i.e., 1 to 3*3

[[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]

Sample Output:

[[0, 0, 0],
  [0, 5, 0],
  [0, 0, 0]]

Sample Input 2: (4x4) i.e., 1 to 4*4

[[ 1,  2,  3,  4],
  [ 5,  6,  7,  8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]]

Sample Output:

[[ 0,  0,  0,  0],
 [ 0,  6,  7,  0],
 [ 0, 10, 11,  0],
 [ 0,  0,  0,  0]]
"""
dimension = int(input("Enter the n dimensions for Square Matrix:"))
square_matrix = np.arange(1,dimension**2+1).reshape(dimension,dimension)
print(f"Before: \n\n{square_matrix}")
square_matrix[[0,-1]] = 0 #updates the first and last row
square_matrix[:,[0,-1]] = 0 #updates the first and last column
print(f"\nAfter: \n\n{square_matrix}")
"""
3. Write a program to print a 2D Array just like a chessboard [0- white color;1- black color]
"""
chess = np.zeros((5,5))
chess[1::2,::2] = 1
chess[0::2,1::2] = 1
print(chess)