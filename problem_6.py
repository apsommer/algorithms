def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # catch bad input: less than one element in passed list
    if len(ints) < 1:
        print("Input list must contain at least one integer.")
        return

    # catch bad input: elements out of range
    for element in ints:
        if not isinstance(element, int) or element < 0 or element > 9:
            print("Input must be a list of integers i, where 0 < i < 9.")
            return

    # step through the array and capture the smallest and largest elements using simple comparison

    # start the min and max storage variables at the first element
    min = ints[0]
    max = ints[0]

    # loop over the input list
    for element in ints:

        # current element is less than min, up min
        if element < min:
            min = element

        # current element is greater than max, update max
        if element > max:
            max = element

    return (min, max)

########## TESTING
import random
l = [i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass
print("Pass" if ((0, 5) == get_min_max([3, 0, 1, 2, 4, 5, 3])) else "Fail")
# Pass
print("Pass" if ((4, 4) == get_min_max([4])) else "Fail")
# Pass
get_min_max([])
# Input list must contain at least one integer.
get_min_max(["apples"])
# Input must be a list of integers i, where 0 < i < 9.
