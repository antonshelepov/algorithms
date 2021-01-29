from nose.tools import assert_equal

def sent_rev(sent):

    words = sent.split(" ")
    words = [w.strip() for w in words if w]

    return words[::-1]

def sent_rev2(sent):

    return " ".join(reversed(sent.split()))

def sent_rev3(sent):

    return " ".join(sent.split()[::-1])


if __name__ == "__main__":

    class ReversalTest(object):
    
        def test(self,sol):
            assert_equal(sol('    space before'),'before space')
            assert_equal(sol('space after     '),'after space')
            assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
            assert_equal(sol('1'),'1')
            print("ALL TEST CASES PASSED")
        
    # Run and test
    t = ReversalTest()
    t.test(sent_rev3)