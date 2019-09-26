# Autocomplete with Tries

The problem statement and general discussion are in jupyter notebook `problem_5.ipynb`.

#### Data Structures

The data structure explored in this problem is the [Trie](https://en.wikipedia.org/wiki/Trie), also called a digital tree or prefix tree. This is an ordered tree-like structure composed of nodes. Each node contains a hashmap of other nodes, with no limit on the number of children a node may have. This data structure is ideal for sequential data sets such as words, directories, or other hierarchies.

#### Time Complexity

Each method requires independent analysis.

For the node class, insert requires O(1) time by inspection. The suffixes method is recursive and depends on size the trie itself rather the input size. Let m = number of nodes in the subtrie under the desired prefix ending, then the method requires O(m) time.

For the trie class, both insert and find require O(n) time, where n = number of characters in the input word, n nodes are traversed to find or insert a complete word of n characters.

For the total time complexity of the testing code we have the linear O(n) of the initial prefix find, and then O(m) for the suffixes method. This results in a total time of O(mn), where m = number of suffixes in the subtrie below a given node, n = number of characters in the prefix.

#### Space Complexity

Each method requires independent analysis.

For the node class, insert is constant space O(1). The suffixes method is recursive and therefore has a space penalty relative to its equivalent iterative implementation. As with time complexity, space complexity is dependent on the number of nodes in the subtrie underneath a given prefix ending character. Let m = number of nodes in the subtrie under the desired prefix ending, then the method requires O(m) space to execute. In the worst case, m is the total number of entries in the trie starting from the root.

For the trie class, both insert and find are constant space O(1). Although we are traversing down a subtrie in each case, these methods use iteration and therefore the temporary variables used in each loop are discarded on each new iteration.

For the total space complexity of the testing code the analysis is similar to time complexity. We have O(1) for the initial prefix find since this is iterative, and O(m) for the suffix method since it is recursive. Therefore, the total space complexity to run the autocomplete widget is O(m).
