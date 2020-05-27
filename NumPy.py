import numpy as np

l = [1,2]
nplist = np.array(l)
print (nplist)

b = [9.0,8.0,7.0], [6.0,5.0,4.0]
nplist_twod = np.array(b)
print (nplist_twod)

#Get Dimension of Numpy Array

print (nplist.ndim)
print (nplist_twod.ndim)

#Gte shape

print (nplist.shape)
print (nplist_twod.shape)

#Get Type

print (nplist.dtype)
print (nplist_twod.dtype)

#Get Size

print (nplist.itemsize)
print (nplist_twod.itemsize)

#Acessing/ Changing Specific Elements, Rows, Columns, etc

a = [1,2,3,4,5,6,7], [8,9,10,11,12,13,14]
anp = np.array(a)
print (anp)
#Get to a specific element [r,c]
print (anp [1, 5])
#Remember, we start indexing at 0!

#Get a specific row
print (anp[1,:])

#Get a specific column
print (anp[:,1])

#Getting a little more fancy [startindex: endindex: stepsize]
print (anp [0, 1:6:2])

 #Changing elements
anp [1,5] = 20
print (anp)

anp [:,2] = 5
print (anp)

#3-D Example
c = [[1,2], [3,4]], [[5,6],[7,8]]
nplist_threed = np.array(c)
print (nplist_threed)

#Get specifc element (work outside in
print (nplist_threed[0,1,1])

#Initializing Different Types of Arrays
#All 0s matrix
print (np.zeros((2,3)))

#All ones matrix
print (np.ones((4,2,2), dtype= 'int32'))

#Any other number
print (np.full((2,2), 99))

#Any other number (full_like)
print ((np.full_like (anp,4)))
print ((np.full (anp.shape,4))) #These two lines of code are equivalent

#Random decial numbers
print (np.random.rand(4,2,3))

#Random Integer Values
print (np.random.randint(7, size = (3,3)))

#Identity Matrix
print (np.identity(5))

#Repeat array
arr = np.array([1,2,3])
r1 = np.repeat(arr,3)
print (r1)

#Challenge
matrix1= np.zeros((5,5))
matrix1 [0,:] = 1
matrix1 [4,:] = 1
matrix1 [:, 0] = 1
matrix1 [:, 4] = 1
matrix1 [2,2] = 9
print (matrix1)

#Be careful when copying arrays!

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print (a)
print (b)

#Mathematics
f = np.array([1,2,3,4])
print (f)
print (f+2)
print(f-2)
#Powers
print (f**2)
#sine
print (np.sin(f))

#Linear Algebra
linmatrix1 = np.ones((2,3))
print (linmatrix1)

linmatrix2 = np.full((3,2), 2)
print (linmatrix2)

print (np.matmul(linmatrix1,linmatrix2))

#Find the determinate
j = np.identity(30)
print (np.linalg.det(j))

#Stats
stats = np.array([[1,2,3], [4,5,6]])
print (np.min(stats))
print (np.max(stats))
print (np.average(stats))

#Reorganizing Arrats
before = np.array([[1,2,3,4],[5,6,7,8]])
print (before)

after = before.reshape((8,1))
print (after)

#Vertical Stacks
v1 = np.array([1,2,3,4])
v2 = np.array ([5,6,7,8])
print (np.vstack([v1,v2]))

#Horizontal Stacks
print (np.hstack([v1,v2]))

#Misc
#Load Data Into File
data = np.genfromtxt('data.txt', delimiter = ',')
data = data.astype('int32')
print (data)

#Boolean Masking and Advanced Indexing

print (data> 50)
print (data[data> 50])
print ((data > 50) & (data < 100))
print (~(data > 50) & (data < 100))

