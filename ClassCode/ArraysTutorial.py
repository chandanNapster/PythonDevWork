list = [1,2,4,5,6,8.5]
##print(list)



##ARRAYS IN PYTHON
##In Python there are two types of Arrays
##Inbuilt arrays which are called array arrays
##And we can also use array in the Package NumPy (NumPy Arrays)

import numpy as np
a = np.array(list)
print(a)

##ARRAYS can only hold a single data type
##Therefore, adding the list to array a converted all the elements to strings

print(list.pop())
print(round(a.mean()))
print(a.mean())



##SLICING ARRAYS
print(list[0:len(list)])


print(a[2:4:2])

print(a)
b = a[1:3]

print(b)

b[1] = 20

print(b)

print(a)
##AN IMPORTANT THING TO LEARN ABOUT ARRAYS
##WHEN ASSIGNING A VARIABLE TO AN ARRAY THE NEW VARIABLE KEEPS A REFERENCE TO THE OLDER ARRAY
##ANY CHANGES DONE TO THE VARIABLE HOLDING THE ARRAY WILL BE REFLECTED IN THE ACTUAL ARRAY
##USE c = a.copy() to copy array a into a different array c

c = a.copy()

print(c)

c[1] = 3000

print(c)
print(a)
