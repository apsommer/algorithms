def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    c = 0
    z = 0
    t = len(input_list) - 1

    while c <= t:

        current = input_list[c]
        last_zero = input_list[z]
        last_two = input_list[t]

        # zero, swap with the last zero
        if current == 0:

            input_list[c] = last_zero
            input_list[z] = current

            z += 1
            c += 1

        # one, do nothing
        if current == 1:
            c += 1

        # two, swap with the last two
        if current == 2:

            input_list[c] = last_two
            input_list[t] = current

            t -= 1

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
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
