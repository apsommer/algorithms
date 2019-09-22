def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # type check input: must be a clean list of integers > 0
    for element in input_list:
        if not isinstance(element, int) or element < 0:
            print("Input must be a list of integers > 0.")
            return

    # start recursive mergesort over the entire breath of the input list
    sorted_input = mergesort(input_list, 0, len(input_list) - 1)

    # the sorting above is 90% of this problem, the remaining logic simply steps
    # through the sorted array, backwards, building two strings using simple
    # concatenation, these strings are then converted back to integers and output

    # temporary strings built while stepping through the sorted array
    one = ""
    two = ""

    # loop through the sorted array backwards, one element at a time
    for i in range(len(sorted_input) - 1, -1, -1):

        # get the current element
        element = sorted_input[i]

        # index is even, add to "one"
        if i % 2 == 0:
            one += str(element)

        # index is odd, add to "two"
        else:
            two += str(element)

    # convert strings to integers, isn't python great? :)
    one = int(one)
    two = int(two)

    # return the output in the specified format
    if one > two:
        return [one, two]
    return [two, one]

# move a single "pivot" element to its final sorted location in the list
def move_pivot(input, s, p):

    # either the pivot index p, or the start index s, move on each iteration

    # base case: the indexes are pointing to the same element
    if p == s:
        return p

    # get the element values at these indexes
    start = input[s]
    pivot = input[p]

    # if the pivot value is less than the start value, rotate three elements
    # resulting in the pivot moving back one index
    if pivot < start:

        # one less than pivot to start, pivot back one, start to pivot
        input[s] = input[p - 1]
        input[p - 1] = pivot
        input[p] = start

        # move the pivot index back one to reflect the change and prepare for
        # next level of recursion
        p -= 1

    # else don't move any elements, but consider one element to the right of
    # start on the next level of recursion
    else:
        s += 1

    # drive all the way down to the base case, and return it all the way up
    return move_pivot(input, s, p)

# recursive method considers the passed end index as the pivot and moves it
# to its final, sorted location
def mergesort(input, s, e):

    # after the pivot is placed, the sublist to the left of the pivot and the
    # sublist to the right are sent back through mergesort() to have their
    # pivots (ending elements) moved to their correct final positions

    # base case: starting and ending indexes have crossed one another
    if e <= s:
        return

    # move the ending element (pivot) and return its final location
    p = move_pivot(input, s, e)

    # mergesort the left remaining sublist
    mergesort(input, s, p - 1)

    # mergest sort the right remaining sublist
    mergesort(input, p + 1, e)

    return input

########## TESTING
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass
print(rearrange_digits([7, 4, 94, 82, 1, 0]))
# [9471, 8240]
print(rearrange_digits([4, 6, 2, 5, 9, 8, 14, 22, 0, 23]))
# [2314852, 229640]
rearrange_digits("apples")
# Input must be a list of integers > 0.
rearrange_digits([4, "apples", 2, 16])
# Input must be a list of integers > 0.
rearrange_digits([-1, 4, 3, 5])
# Input must be a list of integers > 0.
