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
        if not isinstance(element, int) or element < 0 or element > 9:
            print("Input must be a list of positive integers i, where 0 < i < 9.")
            return

    # start recursive quicksort over the entire breath of the input list
    sorted_input = quicksort(input_list, 0, len(input_list) - 1)

    # the sorting above is 90% of this problem, the remaining logic simply steps through the sorted array, builds two integers using essentially integer concatenation

    # variables for the output and the 10^n multiplier
    one = 0
    two = 0
    base_10 = 1

    # loop through the sorted array
    for i in range(len(sorted_input)):

        # get the current element
        element = sorted_input[i]

        # index is even, add to "one"
        if i % 2 == 0:
            one += element * base_10

        # index is odd, add to "two"
        else:
            two += element * base_10
            base_10 *= 10

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
def quicksort(input, s, e):

    # after the pivot is placed, the sublist to the left of the pivot and the
    # sublist to the right are sent back through quicksort() to have their
    # pivots (ending elements) moved to their correct final positions

    # base case: starting and ending indexes have crossed one another
    if e <= s:
        return

    # move the ending element (pivot) and return its final location
    p = move_pivot(input, s, e)

    # quicksort the left remaining sublist
    quicksort(input, s, p - 1)

    # mergest sort the right remaining sublist
    quicksort(input, p + 1, e)

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
print(rearrange_digits([7, 4, 9, 8, 1, 0]))
# [971, 840]
print(rearrange_digits([4, 6, 2, 5, 9, 8, 1, 0, 2, 4]))
# [96421, 85420]
rearrange_digits("apples")
# Input must be a list of positive integers i, where 0 < i < 9.
rearrange_digits([4, "apples", 2, 16])
# Input must be a list of positive integers i, where 0 < i < 9.
rearrange_digits([-1, 4, 3, 5])
# Input must be a list of positive integers i, where 0 < i < 9.
rearrange_digits([42, 4, 3, 5])
