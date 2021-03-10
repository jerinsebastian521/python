class Rectangle:
    def __init__(self, b, l):
        self.b = b
        self.l = l

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


l = int(input("enter length of 1st rectangle:"))
b = int(input("enter breadth of 1st rectangle:"))
arr = Rectangle(l, b)
print("area of 1st rectangle", arr.area())

l = int(input("enter length of 2nd rectangle:"))
b = int(input("enter breadth of 2nd rectangle:"))
ar = Rectangle(l, b)

print("area of 2nd rectangle", ar.area())

print("1st rectangle perimeter=", arr.perimeter())
print("2nd rectangle perimeter=", ar.perimeter())

r1 = arr.area()
r2 = ar.area()

if r1 > r2:
    print("area of 1st rectangle is greater")
else:
    print("area of 2nd rectangle is greater")
