from nose.tools import assert_equal

def finder(arr1, arr2):

    arr1.sort()
    arr1.sort()

    for n1, n2 in zip(arr1, arr2):
        if n1 != n2:
            return n1

    return arr1[-1]


if __name__ == "__main__":

    # finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])


    class TestFinder(object):
        
        def test(self,sol):
            assert_equal(sol([5,5,7,7],[5,7,7]),5)
            assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
            assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
            print('ALL TEST CASES PASSED')

    # Run test
    t = TestFinder()
    t.test(finder)