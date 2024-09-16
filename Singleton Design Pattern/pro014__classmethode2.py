class Mosalas:
    area = 50
    @classmethod
    def printarea(cls):
        print("masahat in mosalas hast:",cls.area)

#Mosalas.printarea = classmethod(Mosalas.printarea)
Mosalas.printarea()

#class Mosalas:
#    def __init__(self,area):
#        self.area = area
#    def printarea(self):
#        print("masahat in mosalas hast:",self.area)
#
#p=Mosalas(50)
#p.printarea()