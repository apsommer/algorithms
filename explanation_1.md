# Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(27) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`

### Solution

problem_1.py

#### Data Structures

This particular problem is fairly simple and does not contain any custom or built-in data structures. It only manipulates primitive integer data types. A binary search technique is used to continuously multiplying an integer by 1/2 until a desired value is found.

#### Time Complexity

Due to the binary search technique this algorithm has O(log(n)) time. On each recursive level we consider 1/2 of the previous level's input range, meaning each level has (1/2)^n elements. Applying log base 2 to this expression reveals the log(n) order of the solution.

#### Space Complexity

Space complexity is also O(log(n)). We need to store two integers (mid, square) in memory for each level of recursion, and there are log(n) recursive levels needed to find the solution. In this case, space complexity follows the same pattern as time complexity.
