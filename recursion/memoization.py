# Memoization refers to remembering results of method calls based on the method inputs and then returning the remembered result rather than computing the result again

factorial_memo = {}

def factorial(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)

    return factorial_memo[k]

print(factorial(4))

print(factorial_memo) 
