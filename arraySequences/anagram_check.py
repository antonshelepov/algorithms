from nose.tools import assert_equal

def anagram(s,t):
    """
    :type s: str
    :type t: str
    rtype: bool
    """
    s=s.replace(' ','').lower()
    t=t.replace(' ','').lower()

    if(len(s)!=len(t)):
        return False

    counter = {}

    for letter in s:
        if letter in counter:
            counter[letter] +=1
        else:
            counter[letter] =1

    for letter in t:
        if letter in counter:
            counter[letter] -=1
        else:
            return False

    for k in counter:
        if counter[k]!=0:
            return False

    return True

if __name__ == "__main__":

    #print(anagram("dog","god"))

    class AnagramTest(object):
        
        def test(self,sol):
            assert_equal(sol('go go go','gggooo'),True)
            assert_equal(sol('abc','cba'),True)
            assert_equal(sol('hi man','hi     man'),True)
            assert_equal(sol('aabbcc','aabbc'),False)
            assert_equal(sol('123','1 2'),False)
            print('ALL TEST CASES PASSED')

    # Run Tests
    t = AnagramTest()
    t.test(anagram)