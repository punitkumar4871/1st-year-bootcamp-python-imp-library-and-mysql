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
