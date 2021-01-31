from nose.tools import assert_equal

#def uni_char(item):
#    return len(set(item)) == len(item)

def uni_char(item):
    u = set()

    for i in item:
        if i in u:
            return False
        else:
            u.add(i)
    return True

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('all done')

t = TestUnique()
t.test(uni_char)
