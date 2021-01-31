from nose.tools import assert_equal
import pprint

def compress(item):
    
    length = len(item)
    if l == 0:
        return ""
    if l == 1:
        return item
    
    counter = {}

    for i in item.split():
        if i not in counter:
            counter[i] +=1
        else:
            counter[i] =1

    return counter


pprint.pprint(compress("AAAaaB")
#class TestCompress(object):
#
#    def test(self, sol):
#        assert_equal(sol(''), '')
#        assert_equal(sol('AABBCC'), 'A2B2C2')
#        assert_equal(sol('AAABCCDDDD'), 'A3B1C2D5')
#        print("all tests passed")
#
#
#t = TestCompress()
#t.test(compress)
