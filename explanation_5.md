# Autocomplete with Tries

The problem statement and general discussion are in jupyter notebook `problem_5.ipynb`.

#### Data Structures

The data structure explored in this problem is the [Trie](https://en.wikipedia.org/wiki/Trie), also called a digital tree or prefix tree. This is an ordered tree-like structure composed of nodes. Each node contains a hashmap of other nodes, with no limit on the number of children a node may have. This data structure is ideal for sequential data sets such as words, directories, or other hierarchies.

#### Time Complexity

Each method requires independent analysis.

For the node class TrieNode(), insert() requires O(1) time by inspection. The suffixes() method is recursive and depends on size the trie itself rather the input size. Let m = number of nodes in the subtrie under the desired prefix ending, then the method requires O(m) time.

For the trie class Trie(), both insert() and find() require O(n) time, where n = number of characters in the input word. We traverse n nodes to find or insert a complete word of n characters.

#### Space Complexity

Each method requires independent analysis.

For the node class TrieNode(), insert() is constant space O(1). The suffixes() method is recursive and therefore has a space penalty relative to its equivalent iterative implementation. As with time complexity, space complexity is dependent on the number of nodes in the subtrie underneath a given node (prefix ending). Let m = number of nodes in the subtrie under the desired prefix ending, then the method requires O(m) space to execute.

For the trie class Trie(), both insert() and find() are constant space O(1). Although we are traversing down a subtrie in each case, these methods use iteration and therefore the temporary variables used in each loop are discarded on each new iteration.
