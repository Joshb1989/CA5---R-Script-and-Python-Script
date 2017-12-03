#Create lists
a = [1,2,5,10,20]
b = [2,4,10,15,30]

class Calculator(object):

#1st function
    def square(self, x):
        map(lambda x : x**2, a)
        return square(x)

#2nd function
    def cube(self, x):
        map(lambda x : x**3, a)
        return cube(x)

#3rd function
    def squareroot(self, x):
        map(lambda x : x**0.5, a)
        return squareroot(x)

#4th function
    def cuberoot(self, x):
        map(lambda x : x**0.3333333, a)
        return cuberoot(x)
        
#5th function
    def divide(self, x, y):
        if y == 0:
            return 'nan'
        map(lambda x,y : x/float(y), a,b)
        return divide(x,y)

#6th function
    def multiply(self, x, y):
        map(lambda x,y : x*y, a,b)
        return multiply(x,y)

#7th function
    def add(self, x, y):
        map(lambda x,y : x+y, a,b)
        return add(x,y)

#8th function
    def subtract(self, x, y):
        map(lambda x,y : x-y, a,b)
        return subtract(x,y)

#9th function
    def exp(self, x, y):
        map(lambda x,y : x*(10**y), a,b)
        return exp(x,y)

#10th function
    def inv(self, x):
        if x == 0:
            return 'nan'
        map(lambda x : 1/float(x), a)
        return inv(x)

