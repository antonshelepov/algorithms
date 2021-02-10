def fact(n):
    """this method returns factorial of n (n!)
    """

    if n == 0:
        return 1

    else:
        return n * fact(n-1)

def sum_func(n):
    """this method returns the sum of all the individual digits in that integer
    """
    if (n<10):
        return n
    else:
        return n%10 + sum_func(int(n/10))
    pass

def word_split(phrase,wordList,output = None):
    if output is None:
        output = []

    for word in wordList:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], wordList, output)
    return output
