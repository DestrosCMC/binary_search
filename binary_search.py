#!/bin/python3


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if not xs:
        return None
    if xs:
        if xs[0] > 0:
            return 0

    if len(xs) == 1:
        if xs[0] > 0:
            return 0
        else:
            return None

    if len(xs) == 2:
        if xs[0] and xs[1] < 0:
            return None
        if xs[0] > 0:
            return 0
        elif xs[1] > 0:
            return 1

    if xs[-1] < 0:
        return None

    def _b_zero_search(arr, num):
        high = len(arr) - 1
        mid = 0
        low = 0

        while low <= high:
            mid = (high + low) // 2

            if arr[mid] < num:
                low = mid + 1

            elif arr[mid] > num:
                high = mid - 1
            else:
                return mid
        return None

    if 0 not in xs and xs[-1] > 0:
        for i in range(1, 20):
            a = _b_zero_search(xs, i)
            if a:
                return a

    index = None

    b_search = _b_zero_search(xs, 0)

    if b_search < len(xs):
        index = b_search + 1
        return index

    '''
    if len(xs) == 1:
        if xs[0] > 0:
            return 0
        else:
            return None

    if len(xs) == 2:
        if xs[0] and xs[1] < 0:
            return None
        if xs[0] > 0:
            return 0
        elif xs[1] > 0:
            return 1

    first = 0
    last = len(xs) - 1
    found = False
    ans = None

    while first <= last and not found:
        midpt = (first + last) // 2
        if xs[midpt] == 0:
            found = True
            if midpt + 1 <= len(xs):
                ans = midpt + 1
            else:
                ans = None

        else:
            if 0 < xs[midpt]:
                last = midpt - 1
            else:
                first = midpt+1
    return ans
    '''


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    high = len(xs)
    low = 0
    n = len(xs)
    xs.reverse()

    if x not in xs:
        return 0

    def first(xs, low, high, x, n):
        if high >= low:
            mid = low + (high - low) // 2
            if ((mid == 0 or x > xs[mid - 1]) and xs[mid] == x):
                return mid
            elif (x > xs[mid]):
                return first(xs, (mid + 1), high, x, n)
            else:
                return first(xs, low, (mid - 1), x, n)
        return -1

    def last(xs, low, high, x, n):
        if (high >= low):
            mid = low + (high - low) // 2
            if ((mid == n - 1 or x < xs[mid + 1]) and xs[mid] == x):
                return mid
            elif (x < xs[mid]):
                return last(xs, low, (mid - 1), x, n)
            else:
                return last(xs, (mid + 1), high, x, n)
        return -1
    return last(xs, low, high, x, n) - first(xs, low, high, x, n) + 1


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float
    as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value
    that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest,
               you recursively call your function on the
               interval [lo,m2] or [m1,hi]

    APPLICATION:
    Essentially all data mining algorithms are
    just this argmin implementation in disguise.
    If you go on to take the data mining class (CS145/MATH166),
    we will spend a lot of time talking about different
    f functions that can be minimized and their applications.
    But the actual minimization code will
    all be a variant of this binary search.

    WARNING:
    The doctests below are not intended to pass on your code,
    and are only given so that you have an example
    of what the output should look like.
    Your output numbers are likely to be slightly
    different due to minor implementation details.
    Writing tests for code that uses floating
    point numbers is notoriously difficult.
    See the pytests for correct examples.

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    '''
    if hi - lo < epsilon:
        if min(f(lo), f(hi)) == f(lo):
            return lo
        if min(f(lo), f(hi)) == f(hi):
            return hi
    '''

    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    if hi - lo < epsilon:
        return hi
    if f(m1) > f(m2):
        return argmin(f, m1, hi, epsilon)
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)

    '''
    #if not hi - lo < epsilon:
    m1 = lo  - (hi - lo) / 3

    m2 = hi + (hi - lo) / 3
    if  min(f(m1), f(m2), f(lo), f(hi)) == f(m1) or f(lo):
        return argmin(f, lo, m2, epsilon)
    if min(f(m1), f(m2), f(lo), f(hi)) == f(m2) or f(hi):
        return argmin(f, m1, hi, epsilon)
    '''
######################################
# the functions below are extra credit
######################################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum
    is guaranteed to be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''
    return


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it
    internally uses the find_boundaries function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
