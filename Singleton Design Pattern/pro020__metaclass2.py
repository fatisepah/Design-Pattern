class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("int eejad shode:", args)
        return type.__call__(cls, *args, **kwargs)
    
# به جای cls خود MyInt میشنه
class int(metaclass = MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = int(10, 20)