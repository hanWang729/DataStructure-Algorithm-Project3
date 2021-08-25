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

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

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