class A:
    #def hablar(self):
    #    print("Habla A")
    pass

class F:
    def hablar(self):
        print("Habla F")

class B(A):
    #def hablar(self):
    #    print("Habla B")
    pass

class C(F):
    #def hablar(self):
    #    print("Habla C")
    pass

class D(B,C):
    #def hablar(self):
    #    print("Habla D")
    pass


d = D()
d.hablar()

F.hablar(d)

print(D.mro())