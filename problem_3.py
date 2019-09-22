def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    sorted_input = mergesort(input_list, 0, len(input_list) - 1)
    print(sorted_input)

def move_pivot(input, s, p):

    if p == s:
        return p

    start = input[s]
    pivot = input[p]

    if pivot < start:

        input[s] = input[p - 1]
        input[p - 1] = pivot
        input[p] = start

        p -= 1

    else:
        s += 1

    return move_pivot(input, s, p)

def mergesort(input, s, e):

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
