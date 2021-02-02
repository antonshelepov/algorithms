# given a string of opening and closing parantheses, check whether it's balanced.

from nose.tools import assert_equal

def balance_check(item):

    if len(item)%2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching pairs
    matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])

    stack = []

    for i in item:

        if i in opening:
            stack.append(i)
        
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open,i) not in matches:
                return False

    return len(stack) == 0

class TestBalanceCheck(object):
        
    def test(self,sol):
        assert_equal(sol('no par here'), False)
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
                                                    

t = TestBalanceCheck()
t.test(balance_check)
