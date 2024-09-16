from typing import Any


class A:
    def __init__(self):
        print("init A")
    def __call__(self):
        print("call A")


a = A() #init A
a() #call A

#########################################

class B:
    def __init__(self, a, b, c):
        pass

b = B(1,2,3)
#در اینجا instance فراخوانی میشود یعنی در اصل call می شود
class C:
    def __call__(self,a , b , c):
        pass

c = C()

c(1,2,3)
#در اینجا instance مقداردهی اولیه می شود یعنی initialize  می شود