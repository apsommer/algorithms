# Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

**Bonus Challenge #1**: Is it possible to find the max and min in a single traversal?

The provided solution runs in a single traversal.

**Bonus Challenge #2**: Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm?

Yes. One such algorithm is [radix sort](https://en.wikipedia.org/wiki/Radix_sort), also called bucket sort or digital sort. On each pass through the array, the same digit in each multi-digit element is considered. All numbers containing this digit are put into the same bucket, then the next digit is considered, etc. ... For example, the English alphabet has 26 buckets and the common base 10 number set has 10 buckets for integers 0-9. This clever algorithm takes `O(bn)` time, where b is the number of buckets which reduces to linear `O(n)` time.

#### Data Structures

No data structures are required other than the input array and a few primitives.

#### Time Complexity

Time complexity is `O(n)` by inspection. Each element in the array must be compared once in this [linear search](https://en.wikipedia.org/wiki/Linear_search)

#### Space Complexity

Auxiliary complexity is `O(1)` by inspection. This is an in-place traversal without any additional data structures.
