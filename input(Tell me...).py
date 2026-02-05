class X:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        return self.a < other.a

    def __eq__(self, other):
        return self.a == other.a

ob1 = X(10)
ob2 = X(9)
print("Passed Value:", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = X(10)
ob4 = X(9)
print("Passed Value:", ob3.a, ob4.a)
print(ob3 == ob4)