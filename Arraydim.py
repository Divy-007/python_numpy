import numpy 
print("hello")
print(numpy.__version__)
x =  numpy.array([1,2,3,4,5,"heloo"])
print(x)
print(type(x))
y=numpy.array((1,2,3,4,5))
print(y)
print(type(x))
#printing the 3-d array
z = numpy.array([[[1,2,3,],[4,5,6,]] ,[[1,2,3],[4,56,6]]])
print(z)
#we can check how many dimansions are in our array by ndim atribute
print(x.ndim)
print(y.ndim)
print(z.ndim)
#crearing an array of 5 dimension by ndmin parameter and check 
p= numpy.array([3,4,5,6,7],ndmin=5)
print(p)
print(p.ndim)

