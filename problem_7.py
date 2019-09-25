# represents a single node in the trie
class RouteTrieNode:

    # constructor: initialize each node with a child hashmap and a handler string
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    # add a child node
    def insert(self, endpoint):
        self.children[endpoint] = RouteTrieNode()

# stores routes and their associated handlers
class RouteTrie:

    # constructor: initialize the trie with a root node, this is the root path or homepage node
    def __init__(self, handler = None):
        self.root = RouteTrieNode(handler)

    # recursively add nodes to the trie
    def insert(self, endpoints, handler):

        # recursively add nodes to the trie
        def _insert(node, i):

            # get this segment of the path
            endpoint = endpoints[i]

            # if the endpoint does not exist then create a node for it
            if endpoint not in node.children:
                node.insert(endpoint)

            # move to the next node and next endpoint
            node = node.children[endpoint]

            # handler is assigned only to the leaf (deepest) node of this path
            if i == len(endpoints) - 1 :
                node.handler = handler
                return

            _insert(node, i + 1)

        # start recursion from the root and the first endpoint in the full path string
        _insert(self.root, 0)

    # iteratively find node in the trie
    def find(self, endpoints):

        # start at the root
        node = self.root

        # starting at the root, navigate the trie to find a match for this path endpoint
        for endpoint in endpoints:

            # move to next node
            node = node.children.get(endpoint, None)

            # if the node does not exist in the trie return none
            if node == None:
                return None

        # node found, return its handler string
        return node.handler

# the router class wraps the trie
class Router:

    # constructor: create a new trie to hold the routes and a "not found" handler
    def __init__(self, root_handler = None, error_handler = "Error 404 page not found."):
        self.trie = RouteTrie(root_handler)
        self.error_handler = error_handler

    # add handler to a path endpoint
    def add_handler(self, path, handler):

        # catch malformed path
        if not isinstance(path, str) or path[0] != '/':
            print("Invalid path.")
            return

        # catch malformed handler
        if not isinstance(handler, str):
            print("Invalid handler.")
            return

        # split the path and pass the parts as list to the trie
        endpoints = self.split_path(path)
        self.trie.insert(endpoints, handler)

    # return the handler for a given path
    def lookup(self, path):
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # edge case: catch the root
        if path == "/" or "":
            return self.trie.root.handler

        # split the path and pass the parts as list to the trie
        endpoints = self.split_path(path)
        handler = self.trie.find(endpoints)

        # if the endpoint handler was not found return an error message
        if handler == None:
            return self.error_handler

        return handler

    # split path string to a list around the "/" delimiter
    def split_path(self, path):

        # split path string to a list around the "/" delimiter
        endpoints = path.split("/")

        # preceeding and ending "/" cause blank elements, trim them off
        endpoints = endpoints[1:]
        if endpoints[-1] == '':
            endpoints = endpoints[:-1]

        return endpoints

########## TESTING
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")
print(router.lookup("/"))
# root handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/about"))
# about handler
print(router.lookup("/home/about/"))
# about handler
print(router.lookup("/home/about/me"))
# not found handler
router.add_handler("bad_path", "handler")
# Invalid path.
router.add_handler("/apples", 123)
# Invalid handler.
