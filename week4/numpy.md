# Introduction to NumPy

NumPy (Numerical Python) is a fundamental library for numerical operations in Python. It provides efficient support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays.

## Benefits of using NumPy over standard Python lists:
- **Compact and Fast:** NumPy arrays are more compact in memory and faster in execution compared to Python lists.
- **Mathematical Functions:** NumPy provides a wide range of mathematical functions and operations optimized for scientific computing.
- **Integration:** NumPy arrays can be easily integrated with other scientific computing libraries like SciPy and Matplotlib.

## Installing NumPy

You can install NumPy using the Python package installer pip:

``` python
pip install numpy
```

# NumPy Arrays

NumPy arrays are the core data structure in NumPy. They are similar to Python lists but more efficient and optimized for numerical operations.

## Commonly Used NumPy Attributes

### `shape`

The `shape` attribute returns a tuple representing the dimensions of the array.

```python
import numpy as np

# 1D array
u = np.array([1, 2, 3, 4, 5])
print(u.shape)  # Output: (5,)

# 2D array
v = np.array([[1, 2, 3], [4, 5, 6]])
print(v.shape)  # Output: (2, 3)

# 3D array
w = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(w.shape)  # Output: (2, 2, 2)

```
# size of a numpy array
The size attribute returns the total number of elements in the array.
```python
x = np.array([[1, 2], [3, 4], [5, 6]])
print(x.size)  # Output: 6
```
# d-type
dtype: The dtype attribute represents the data type of the array elements.
```python
# Integer array
a = np.array([1, 2, 3, 4, 5])
print(a.dtype) 

# Float array
b = np.array([1.0, 2.0, 3.0])
print(b.dtype)  

# Complex array
c = np.array([1+2j, 3+4j])
print(c.dtype)  

# Boolean array
d = np.array([True, False, True])
print(d.dtype)  
```
# output
''' 
int64
float64
complex128
bool
'''

# Create an array with float32 data type
```python 
a = np.array([1, 2, 3], dtype=np.float32)
print(a)        
print(a.dtype)  
```
# Create an array with int16 data type
```python
b = np.array([1, 2, 3], dtype=np.int16)
print(b)        
print(b.dtype)  
```

# Creating NumPy Arrays

## From a List

You can convert a Python list into a NumPy array using `np.asarray()`:

```python
import numpy as np
# Example from a list
c = [1, 2, 3, 4, 5]
a = np.asarray(c)
print(a)
# Output: [1 2 3 4 5]
```

# From a Tuple
you can convert a Python tuple into a NumPy array:
# Example from a tuple
```python
d = (10, 20, 30)
b = np.asarray(d)
print(b)
# Output: [10 20 30]
```


## Using np.ones()
You can create NumPy arrays filled with ones using np.ones():
# Create a 1D array of ones
```python
a = np.ones(5)
print(a)
# Output: [1. 1. 1. 1. 1.]

# Create a 2D array of ones with shape (3, 4)
b = np.ones((3, 4))
print(b)
# Output:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
```


# NumPy Array Initialization

## `np.zeros()`: Create an array filled with zeros

### 1D Array of Zeros

```python
import numpy as np

# Create a 1D array of zeros
a = np.zeros(5)
print(a)
# Output: [0. 0. 0. 0. 0.]
```

#2D Array of Zeros
```python
# Create a 2D array of zeros with shape (2, 3)
b = np.zeros((2, 3))
print(b)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]
```


# `np.empty()`: Create an uninitialized array
## 1D Uninitialized Array
```python
# Create an uninitialized 1D array
a = np.empty(5)
print(a)
# Output: [0. 0. 0. 0. 0.]
```
# 2D Uninitialized Array
```python
# Create an uninitialized 2D array with shape (2, 3)
b = np.empty((2, 3))
print(b)
```

### NumPy Array Operations

#### Addition
Adds two arrays element-wise.

```python
import numpy as np

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

c = a + b
print(c)  # Output: [3 7 11]
```


# Subtraction
Subtracts one array from another element-wise.

```python
import numpy as np

a = np.array([9, 8, 7])
b = np.array([3, 2, 1])

c = a - b
print(c)  # Output: [6 6 6]
```
# Multiplication
Multiplies two arrays element-wise.

```python
import numpy as np

a = np.array([5, 10, 15])
b = np.array([2, 3, 4])

c = a * b
print(c)  # Output: [10 30 60]
```

In this example:
- **Addition** (`a + b`): Adds corresponding elements of arrays `a` and `b`.
- **Subtraction** (`a - b`): Subtracts elements of array `b` from `a`.
- **Multiplication** (`a * b`): Multiplies elements of arrays `a` and `b`.


### NumPy Array Operations

#### Division
Divides two arrays element-wise.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = b / a
print(c)  # Output: [4.  2.5 2. ]
```


# Scalar Operations
Multiplies or divides each element of the array by a scalar value.

```python
import numpy as np

a = np.array([1, 2, 3])

# Multiplication by scalar
b = a * 2
print(b)  # Output: [2 4 6]

# Division by scalar
c = a / 2
print(c)  # Output: [0.5 1.  1.5]
```
# Square Root (np.sqrt())
Computes the square root of each element in the array.

```python
import numpy as np

a = np.array([1, 4, 9])

b = np.sqrt(a)
print(b)  # Output: [1. 2. 3.]
```

In this example:
- **Division** (`b / a`): Divides corresponding elements of array `b` by `a`.
- **Scalar Multiplication** (`a * 2`): Multiplies each element of array `a` by 2.
- **Scalar Division** (`a / 2`): Divides each element of array `a` by 2.
- **Square Root** (`np.sqrt(a)`): Computes the square root of each element in array `a`.

# Broadcasting

Broadcasting is a powerful mechanism in NumPy that allows arithmetic operations between arrays with different shapes.
It automatically duplicates the smaller array along the missing dimensions to match the shape of the larger array.
This makes it possible to perform operations on arrays with different shapes without explicitly reshaping them.
1D Array and Scalar

# 1D array and scalar
```python
a = np.array([1, 2, 3])
b = 2
c = a + b  
print(c)
[3 4 5]
```
# 2D Array and 1D Array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
c = a + b
print(c)
[[11 22 33]
 [14 25 36]]
# Broadcasting follows certain rules:

If the arrays have the same shape, no broadcasting is necessary, and the operation is performed element-wise.
If the arrays have different shapes, NumPy attempts to broadcast the smaller array's shape to match the larger array's shape.
If the dimensions of the arrays are different, NumPy starts from the trailing dimensions and works backward, prepending 1s to the smaller shape until the shapes match.
If the shapes still don't match after prepending 1s, NumPy raises a ValueError.
## Example Of Where Broadcasting is not possible
# Different shapes: (2, 3) and (3, 2)
```python 
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
c = a + b
```  
