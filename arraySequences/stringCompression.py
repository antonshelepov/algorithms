from nose.tools import assert_equal
import pprint

def compress(item):
    length = len(item)

    if length  == 0:
        return ""
    if length == 1:
        return item

    


#def compress(item):
#    
#    length = len(item)
#    if length  == 0:
#        return ""
#    if length == 1:
#        return item
#    
#    counter = {}
#
#    for i in item:
#        if i in counter:
#            counter[i] +=1
#        else:
#            counter[i] =1
#
#    compressed = "".join(key + str(val) for key, val in counter.items())
#
#    return compressed


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDD'), 'A3B1C2D4')
        print("all tests passed")


t = TestCompress()
t.test(compress)
