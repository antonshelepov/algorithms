# Memoization refers to remembering results of method calls based on the method inputs and then returning the remembered result rather than computing the result again

#factorial_memo = {}
#
#def factorial(k):
#
#    if k < 2:
#        return 1
#
#    if not k in factorial_memo:
#        factorial_memo[k] = k * factorial(k-1)
#
#    return factorial_memo[k]

# memoization encapsulated in a class

class Memoize:
    def __init__(self,f):
        self.f = f
        self.memo = {}
    def __call__(self,*args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def factorial(k):

    if k < 2:
        return 1

    return k * factorial(k - 1)

factorial = Memoize(factorial)

print(factorial(4))
