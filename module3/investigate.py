class MyClass:                              # simple class
    pass

obj = MyClass()                             # fill the class
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():        # scan the __dict__ attribute, looking for all attribute names
        if name.startswith('i'):            
            val = getattr(obj, name)        # use the getattr() function to get its current value
            if isinstance(val, int):
                setattr(obj, name, val + 1) # increment the property's value



print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)