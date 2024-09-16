class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("mikhaym obj ro eejad konim...")
        else:
            print("obj ghablan eejad shode", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
#s1 = Singleton()
print("obj eejad shode",Singleton.getInstance())
s2 = Singleton()
