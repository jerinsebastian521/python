class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):

        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second


a = int(input("enter 1st hour"))
b = int(input("enter 1st min"))
c = int(input("enter 1st sec"))
t1 = Time(a, b, c)

d = int(input("enter 2nd hour"))
e = int(input("enter 2nd min"))
f = int(input("enter 2nd sec"))
t2 = Time(d, e, f)

t3 = t1 + t2
print("sum of two time", t3)
