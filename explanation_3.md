# Rearrange Array Elements

Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

Example: [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

#### Data Structures

Quicksort is an in-place, divide and conquer, sorting algorithm. The only data structure utilized is an array, with integer and string primitives to perform requisite calculations.

#### Time Complexity

The phrase "expected time complexity" is interpreted as "average case complexity" which for quicksort is `O(nlog(n))` as required. This is rather difficult to calculate due to recursion, but can be solved using the [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)). Further discussion [here](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/analysis-of-quicksort). After quicksort, the sorted array is traversed once for O(n), which is less than the total `O(nlog(n))`, therefore the total runtime reduces to `O(nlog(n))`.

#### Space Complexity

The space complexity is the reason quicksort was chosen over mergesort. The worst case time of mergesort is equivalent to the expected time of quicksort at `O(nlog(n))`, however mergesort requires `O(n)` auxiliary space while quicksort only uses `O(1)` auxiliary space. This is a dramatic improvement. The reason that mergesort requires linear space is because it needs temporary arrays at each iteration, and at the lowest level of recursion `n` arrays are used. In contrast, quicksort is an in-place sorting algorithm, meaning the pivot movement is native to the original input array with no other structures being required for temporary storage.

As stated, the above discussion in relative to auxiliary space. To be clear, both the chosen quicksort and its alternate mergesort require O(n) total space. This is because the input list itself requires O(n) space in memory prior to the algorithm even starting. The two integer output itself also grows proportionally with the input size n.
