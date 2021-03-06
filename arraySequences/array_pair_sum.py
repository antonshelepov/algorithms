def pair_sum(arr, k):
    """
    :type array: arr
    :type int: k
    :rtype int
    """
    if len(arr) < 2:
        return

    checked = set()
    res = set()

    for n in arr:

        target = k-n

        if target not in checked:
            checked.add(n)

        else:
            res.add( (min(n,target), max(n,target)) )

    return len(res), res


if __name__ == "__main__":

    print(pair_sum([1,4,3,5,3,2,2],7))
