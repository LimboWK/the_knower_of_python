from library import Base 
# import library

# assert condition(bool), message -> if condition is false the python exec stops and print out the message
assert hasattr(Base, "foo"), "you broke it, you fool !"


class Derived(Base):
    # pass
    # what if foo is not included in Base ? someone can only find this issue 
    # when they call or instance a Derived class on the runtime ? 
    
    def bar(self):
        return 'bar'

