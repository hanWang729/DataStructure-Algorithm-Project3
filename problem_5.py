#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[ ]:


## Represents a single node in the Trie
# class TrieNode:
#     def __init__(self):
#         ## Initialize this node in the Trie
#
#     def insert(self, char):
#         ## Add a child node in this Trie
        
## The Trie itself containing the root node and insert/find functions
# class Trie:
#     def __init__(self):
#         ## Initialize this Trie (add a root node)
#
#     def insert(self, word):
#         ## Add a word to the Trie
#
#     def find(self, prefix):
#         ## Find the Trie node that represents this prefix


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[10]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char=""):
        self.is_word = False
        self.children = {}
        self.char = char

    def insert(self, char):
        self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        word_list = list()
        if self.is_word:
            word_list.append(self.char)
            if not self.children:
                return word_list
        for child in self.children:
            child_list = self.children[child].suffixes()
            for i in range(len(child_list)):
                child_list[i] = self.char + child_list[i]
            word_list += child_list
        return word_list
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    ## Add a word to the Trie

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[11]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[12]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




