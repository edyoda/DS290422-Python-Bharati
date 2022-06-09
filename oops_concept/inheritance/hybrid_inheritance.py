class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(B):
    def c(self):
        print("C")

class D(C):
    def d(self):
        print("D")

class E(B):
    def e(self):
        print("E")