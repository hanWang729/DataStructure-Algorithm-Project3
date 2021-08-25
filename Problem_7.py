# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()


    def insert(self, word_list):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for word in word_list:
            if word == "":
                continue
            if word not in current_node.children:
                current_node.insert(word)
            current_node = current_node.children[word]
        return current_node

    def find(self, word_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for word in word_list:
            if word == "":
                continue
            if word in current_node.children:
                current_node = current_node.children[word]
            else:
                return "Not found handler"
        return current_node.is_handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, word = ""):
        # Initialize the node with children as before, plus a handler
        self.is_handler = "Not found handler"
        self.children = {}
        self.word = word

    def insert(self, word):
        # Insert the node as before
        self.children[word] = RouteTrieNode(word)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, name):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_trie = RouteTrie()
        self.router_trie.root.is_handler = name

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        word_list = self.split_path(path)
        end_node = self.router_trie.insert(word_list)
        end_node.is_handler = handler

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        word_list = self.split_path(path)
        handler = self.router_trie.find(word_list)
        return handler


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        result_list = path.split("/")
        return result_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one