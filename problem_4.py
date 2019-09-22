def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # catch bad input
    if not all(isinstance(x, int) for x in input_list):
        print("Input must be a list of integers i, where i = 0, 1, or 2.")
        return

    # On each iteration we either move a zero to the beginning, do nothing except consider the next element (one), or move a two to the end. The idea is to corectly place the zeros and twos which make the ones automatically placed correctly.

    # create starting indexes
    c = 0 # index of current element
    z = 0 # index of last placed zero
    t = len(input_list) - 1 # index of last place two

    # continue until we encounter the end of the list which is all 2's
    while c <= t:

        # get element values at these indexes
        current = input_list[c]
        last_zero = input_list[z]
        last_two = input_list[t]

        # zero, swap with the last zero
        if current == 0:

            # swap
            input_list[c] = last_zero
            input_list[z] = current

            # increment last zero and current element
            z += 1
            c += 1

        # one, do nothing except increment current element
        if current == 1:
            c += 1

        # two, swap with the last two
        if current == 2:

            # swap
            input_list[c] = last_two
            input_list[t] = current

            # decrement the index of the last placed two
            t -= 1

            # do not move the current element as we want to consider its value on the next iteration

    return input_list

########## TESTING
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
sort_012("apples")
# Input must be a list of integers i, where i = 0, 1, or 2.
sort_012([42, "bananas"])
# Input must be a list of integers i, where i = 0, 1, or 2.
