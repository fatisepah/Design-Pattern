from pro010 import SingletonObject

obj1=SingletonObject()
obj1.filename="log1.txt"
obj1.critical("critical message")
print("print obj1: ",obj1)


obj2=SingletonObject()
obj2.filename="log1.txt"
obj2.critical("critical message")
print("print obj1: ",obj1)

print("print obj2: ",obj2)