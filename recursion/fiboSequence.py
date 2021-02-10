# Implementation of Fibonnaci Sequence in three differen ways

from nose.tools import assert_equal

def fib_rec(n):
    '''fibo seq by using recursion; Big-O -> O(2^n)
    '''
    if n == 0 or n == 1:
        return n

    else:
        return fib_rec(n-1) + fib_rec(n-2)

class TestFib(object):
        
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)

    print('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib_rec)
#t.test(fib_dyn)
#t.test(fib_iter)
