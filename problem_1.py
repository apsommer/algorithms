def sqrt(number):
    """
    Calculate the floored square root of a number ... using binary search recursion

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # type check input to ensure it is integer
    if not isinstance(number, int):
        print("Input must be an integer.")
        return

    # catch trivial cases
    if number == 0 or number == 1:
        return number

    # begin recursion over one half the input span, since a square root
    # is never larger than n//2 for n>2
    return sqrt_recursion(number, 0, number//2)

# recursive algrothim using binary search to achieve the required O(log(n)) time
def sqrt_recursion(number, start, end):

    # calculate a middle number (floor) and its square
    mid = (end + start)//2
    square = mid*mid

    # exact match found this is a perfect square
    if square == number:
        return mid

    # since the square is less than the target, the true root must be in the upper half of remaining numbers
    if square < number:

        # we have recursed as far as possible, since we want the floor value of sqrt(n) the current value of mid is the correct output
        if mid == end - 1:
            return mid

        # recurse into upper half between mid:end
        return sqrt_recursion(number, mid, end)

    # since the square is greater than the target, the true root must be in the lower half of remaining numbers
    if square > number:
        return sqrt_recursion(number, start, mid)

########## TESTING

print("Pass" if (3 == sqrt(9)) else "Fail")
# Pass
print("Pass" if (0 == sqrt(0)) else "Fail")
# Pass
print("Pass" if (4 == sqrt(16)) else "Fail")
# Pass
print("Pass" if (1 == sqrt(1)) else "Fail")
# Pass
print("Pass" if (5 == sqrt(27)) else "Fail")
# Pass
sqrt(None)
# Input must be an integer.
sqrt("apples")
# Input must be an integer.
print(sqrt(42))
# 6

########## ALTERNATIVE SOLUTION

# the following implementation requires O(sqrt(n)) time, too slow based on the stated requirements
# it shows an alternative, iterative, brute force method
def sqrt_iterative(number):
    """
    Calculate the floored square root of a number ... using brute force iteration

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # type check input to ensure it is integer
    if not isinstance(number, int):
        print("Input must be an integer.")
        return

    # trivial case, sqrt(0) = 0
    if number == 0:
        return 0

    # trivial case, sqrt(1) = 1
    if number == 1:
        return 1

    # loop until the square root (integer floor) is found
    i = 2
    while True:

        # compute the square of the counter
        square = i*i

        # an exact match is found, return the counter
        if square == number:
            return i

        # the passed integer was exceeded, return the previous integer counter
        if square > number:
            return i-1

        # increment the counter
        i += 1
