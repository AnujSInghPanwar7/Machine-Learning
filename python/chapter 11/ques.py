# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1,2)
a.show()

b = ThreeDVector(5,4,3)
b.show()

# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

class animals:
    pass
class pets(animals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")

d = dog
d.bark()

# 3. Create a class 'Employee' and add salary and increment properties to it.

class employee:
    salary = 23400
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary*self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = employee()

# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.

print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 28080.0
print(e.increment)

# 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.

class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = complex(1,2)
c2 = complex(3,4)
print(c1+c2)

# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})"


v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)

print(v1 + v2)
print(v1 * v2)



# 6. Write_str_() method to print the vector as follows:
# 7i + 8j +10k

class vector2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vector2(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):
        return vector2(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
        )

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Test
v4 = vector2(1, 2, 3)
v5 = vector2(4, 5, 6)

print(v4 + v5)
print(v4 * v5)

# Assume vector of dimension 3 for this problem.



# 7. Override the_len_() method on vector of problem 5 to display the dimension of the vector.

class vector3:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

v6 = vector3([1,2,3])
print(len(v6))
