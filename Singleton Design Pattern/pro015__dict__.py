class Book:
    _shared_state = {"1":"2"}
    def __init__(self):
        self.x = 150
        self.__dict__ = self._shared_state
        pass


a1 = Book()
a2 = Book()
a1.x = 250

print("book obj 'a1':", a1)
print("book obj 'a2':", a2)
print("obj state 'a1':", a1.__dict__)
print("obj state 'a2':", a2.__dict__)