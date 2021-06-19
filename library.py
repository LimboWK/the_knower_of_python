"""
about metaclass:
All classes are inerited by 'type' metaclass which is not changable. 
type metaclass mainly defines how to init a class with __new__() and __init__()
if a class needs a customized init process not like 'type', we can use type class
to derive a changable NewMetaClass, like BaseMeta below, then override the 
__new__ and __init__ methods to do something, like check if a method exists before
we get error on runtime.

In general, metaclass is a derived class from type that customize the class
init process to fit our needs, so called "class factory", like class is being called
as instance factory.
"""

class BaseMeta(type):
    # __new__ method is a built-in method before __init__, to newly build a 
    # class object, and set its address to self. This can be overrided by __new__ method.
    # all of these steps happen when a class obj is executed. (keep in mind that all the classes are somehow executable in python)
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        if name != 'Base' and not 'bar' in body:
            raise TypeError('bad user class !')
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(self, *a, **kw):
        print('__init_subclass__:', a, kw)
        return super().__init_subclass__(*a,**kw)
"""
class Base:
    # pass 
    def foo(self):
        # print('this is foo function')
        return self.bar()

old_bc = __build_class__

def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined') # do actual check for bar method here.
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__ = my_bc 
#print(__name__)
"""
