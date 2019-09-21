def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # type check input to ensure it it integer
    if not isinstance(number, int):
        print("Input must be an integer.")
        return

    # trivial case, sqrt(0) = 0
    if number == 0:
        return 0

    # trivial case, sqrt(1) = 1
    if number == 1:
        return 1

    # loop until the square root (floor) is found
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
