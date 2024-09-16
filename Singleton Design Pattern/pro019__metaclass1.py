class A(object):
    def my_func(self):
        pass

#metaclass
#A=metaclass1(name,bases,dict)
#A=type(A_name,A_parents,A_methods)

#########################################
def my_func(self):
    pass

A_name = 'A'
A_parents = (object,)
A_methods = {'my_func': my_func}

A=type(A_name,A_parents,A_methods)

#####################################
#دو تا حالت با هم برابرن