from nose.tools import assert_equal

def uni_char(item):
    return len(set(item)) == len(item)

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol('', True))
        assert_equal(sol('goo', False))
        assert_equal(sol('abcdefg', True))
        print('all done')

t = TestUnique()
t.test(uni_char)
