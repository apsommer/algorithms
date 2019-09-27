# Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: `[0, 1, 2, 4, 5, 6, 7]` might become `[4, 5, 6, 7, 0, 1, 2]`

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example:
Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
Output: `4`

#### Data Structures

There are no additional data structures needed to solve this problem. Elements in the passed input list are assigned to integer variables on each level of recursion.

#### Time Complexity

Since this algorithm uses binary search its auxiliary time complexity is O(log(n)). On each recursive level, half the array length is considered relative to the previous level. This power-of-two pattern yields a log(n) runtime. The overall time complexity takes into account the input which is O(n), this term dominates O(log(n)) and therefore the total complexity reduces to O(n).

#### Space Complexity

Auxiliary space complexity is also O(log(n)) for the same reason as time complexity. Variables holding the start, middle, and end elements must be stored for each level of recursion, and there are log(n) levels of recursion needed in the worst case. The overall space complexity takes into account the input which is O(n), this term dominates O(log(n)) and therefore the total complexity reduces to O(n).
