class Book:
    _shared_state = {}
    def __new__(self):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

a1 = Book()
a2 = Book()
a3 = Book()
a1.x = "200"
a1.y = "rangi"
a2.x = "300"
a3.z = "20"

print("book obj 'a1':", a1)
print("book obj 'a2':", a2)
print("book obj 'a3':", a3)
print("obj state 'a1':", a1.__dict__)
print("obj state 'a2':", a2.__dict__)