# HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's [SimpleHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler) which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

The RouteTrie stores handlers under path parts, so remember to split your path around the '/' character.

**Bonus Point #1**: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

**Bonus Point #2**: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

#### Data Structures

The primary data structure in this implementation is the [Trie](https://en.wikipedia.org/wiki/Trie). This data structure is ideal for sequential data sets such as words, directories, or other hierarchies. Each node contains some primitive data and a hashmap who's values are an unlimited number of children nodes. This creates a tree-like structure that can be traversed via key:node pairs. For this particular problem, a router class wraps the trie and its constituent nodes for convenience.

#### Time Complexity

With respect to the node, insertion is constant O(1). With respect to the trie, the recursive insert method is linear O(n), where n = number of segments (endpoints) in the path delineated by the `/` character. Search is also linear time O(n) since we need to traverse n path segments to find a given node. The router class wraps the trie and does not increase the order-of-magnitude time complexity.

#### Space Complexity

With respect to the node, insertion is constant O(1) if no handler is specified. However, for this implementation which treats the handler as a string, the space requirement is O(n) when a handler is passed, where n = number of characters in the string. With respect to the trie, the recursive insert method is O(n) since we need to add n primitive collections to the call stack to create a new endpoint. In contrast, the iterative search method is constant O(1) since for each iteration the primitives are discarded.

With respect to the router, the add_handler method splits the path string and creates a new list of size n, resulting in total O(2n) which still reduces to O(n). The lookup method is an interesting case. The path string is split to a list of n elements for O(n) and then passed to the trie's find method which requires O(1). Therefore, the method doing the work is constant O(1) but to create its input is O(n), where n = the number of segments in the path delineated by `/`.
