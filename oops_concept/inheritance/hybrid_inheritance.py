class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C:
    def c(self):
        print("C")

class D(A,B,C):
    def d(self):
        print("D")

class E(B):
    def e(self):
        print("E")