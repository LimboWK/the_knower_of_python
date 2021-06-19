# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# this is a follow-up notebook on the video:https://www.youtube.com/watch?v=7lmCu8wz8ro&t=805s
# which shows a model-oriented python tutorial


# %%
class poly:
    def __init__(self, *coefffs):
        self.coeffs = coefffs
    
    def __add__(self, other):
        # add two poly and return a new poly
        # in case that two polys are not in the same order, we need to use the higher order one as a base.abs
        # like (1,2,3,4)+(1,2,3) = (1,3,5,7)
        if len(self.coeffs) < len(other.coeffs):
            #for i in range(len(self.coeffs)):
                
            return poly(*(self.coeffs[i]+other.coeffs[i] for i in range(len(self.coeffs))))
        else:
            return poly(*(self.coeffs[i]+other.coeffs[i] for i in range(len(other.coeffs))))
        
    def __value__(self,x):
        value = 0
        print("current poly coeffs are:"+str(self.coeffs))
        print("required x is:"+str(x))
        for k, coeff in enumerate(self.coeffs):
               value += coeff*x**k
        return value








