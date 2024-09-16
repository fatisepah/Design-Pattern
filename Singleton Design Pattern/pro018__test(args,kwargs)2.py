def test_argument_kw(**kwargs):
    
    if kwargs is not None:
        for key, value in kwargs.items():
            #print("key:", key, "value:", value)
            print("{0} == {1}".format(key, value))


test_argument_kw(name="ali", age=25) 