from nose.tools import assert_equal

def sent_rev2(sent):

    return " ".join(reversed(sent.split()))

def sent_rev3(sent):

    return " ".join(sent.split()[::-1])

def sent_rev(sent):
    """ Manually doing the splits on the spaces
    """
    words = []
    length = len(sent)
    spaces = [" "]

    # Index Tracker
    i = 0
    while i < length:

        if sent[i] not in spaces:

            # index at which a word starts
            word_start = i
             
            while i < length and sent[i] not in spaces:

                # iterate to the end of a word
                i +=1

            words.append(sent[word_start:i])
        
        i +=1

    return " ".join(reversed(words))

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