# represents a single node in the trie
class RouteTrieNode:

    # constructor: initialize each node with a child hashmap and a handler string
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    # add a child, where all children are hashmap pairs char:node
    def insert(self, char):
        self.children[char] = RouteTrieNode()

# stores routes and their associated handlers
class RouteTrie:

    # constructor: initialize the trie with a root node, this is the root path or homepage node
    def __init__(self):
        self.root = RouteTrieNode()

    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    def insert(self, path):

        node = self.root

        def _insert(node, path):

            

        _insert(node, path)

    def find(self, ...):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match



# The Router class will wrap the Trie and handler
class Router:
    def __init__(self, ...):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, ...):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, ...):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, ...):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

#####################################

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
