def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # start recursive mergesort over the entire breath of the input list
    sorted_input = mergesort(input_list, 0, len(input_list) - 1)
    print(sorted_input)

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

    # TODO more comments

    if e <= s:
        return

    p = move_pivot(input, s, e)
    print(input)

    mergesort(input, s, p - 1)
    mergesort(input, p + 1, e)

    return input















def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
rearrange_digits([4, 6, 2, 5, 9, 8, 14, 22, 0, 23])
