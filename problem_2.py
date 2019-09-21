def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # type check input list
    if len(input_list) == 0:
        print("Passed array has no elements!")
        return

    # type check input target
    if not isinstance(number, int):
        print("Target must be an integer.")
        return

    # start recursion over full length of passed array
    return binary_search(input_list, number, 0, len(input_list) - 1)

# binary search through "pivoted" array
def binary_search(input_list, number, s, e):

    # calculate a middle index
    m = (s + e)//2

    # get the three elements of interest
    start = input_list[s]
    mid = input_list[m]
    end = input_list[e]

    # base case: target found
    if number == mid:
        return m

    # base case: array exhausted target does not exist
    if mid == end:
        return -1

    # target is on the left side of the middle element
    if (start < mid and number < mid) or (start > mid and number >= start):
        return binary_search(input_list, number, s, m - 1)

    # target is on the right side of the middle element
    else:
        return binary_search(input_list, number, m + 1, e)

# linear search finds the correct index in O(n) time
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

# simple testing function
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

########## TESTING
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass
rotated_array_search([6, 7, 8, 1, 2, 3, 4], "apples")
# Target must be an integer.
rotated_array_search([], 42)
# Target must be an integer.
