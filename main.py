#
# * NumPy
#

# NumPy, short for Numerical Python, is a foundational library in Python
# used for numerical and scientific computing. It provides support for large,
# multi-dimensional arrays and matrices, along with a collection of
# mathematical functions to operate on these data structures efficiently.

# ? Why is NumPy important for data science:

# 1. Implemented in C and is highly optimized for performance
# 2. Building block for many other data science libraries, such as Pandas
# 3. Built-in support for a range of mathematical operations, such as linear algebra, Fourier transforms, statistical functions, and more

import numpy as np

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matrix = 2 dimensional array

print("array(): Display a two dimensional array\n", np.array(my_matrix))

print("arange(): Generate an array\n", np.arange(0, 11, 2))  # (start, end, skip)

print(
    "zeros(): Generate a two dimensional array with zero\n", np.zeros((2, 3))
)  # ((row, column)) # or np.ones with ones

print("linspace(): Generate an array with points\n", np.linspace(0, 5, 10))

print("eye(): Generate an array with ones as diagonal\n", np.eye(5))

print(
    "random.rand(): Generate one or two dimensional array with random number\n",
    np.random.rand(5, 5),
)

print(
    "random.randn(): Generate one or two dimensional array with random number\n",
    np.random.randn(5, 5),
)

print(
    "random.randint(): Generate random integer or an array of random interger\n",
    np.random.randint(1, 100, 5),
)
