# Data Structure & Algorithm Project 3

This is project 3 of Udacity's nanoprogram: Data Structure and Algorithm

##  Problem 1: Finding the Square Root of an Integer

Since the root of a number can't bigger than itslef (for a passive interger). 

So I use binary search, set upper bound and lower bound of results. Make the two bounds get close and then finally find the root.

**Time Complexity:** O(logn)

**Space Complexity**: O(1)



## Problem 2: Search in a Rotated Sorted Array

I use the thought of divide and conquer: divide the array into two part. At least one part is sorted array. 

If the sub-array is sorted, just use a normal binary search to the problem, if not, divide it further, until there is only one item left.

**Time Complexity:** O(logn)

**Space Complexity:** O(logn)

*Since you are using a modified **Recursive Binary Search** in your solution code for the search functionality in the rotated array, the space complexity should be logarithmic (i.e. O(log(N)) ) here.*



## Problem 3: Rearrange Array Elements

1. Sort the array by quick sort
2. arrange the number in the array from the biggest to the smallest. give the number to two result one by one. then the sum is the maximum

**Time Complexity:** O(nlogn)

**Space Complexity**: O(n)



## Problem 4: Dutch National Flag Problem

This problem is similar to the idea of quick sort. Just use two pivot. if the number is 0, put it at the left of pivots, if 2, put it at the right of pivots, if 1 put it at the middle of pivots.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

*Since you are not using any extra/auxiliary space, here, it should be constant,i.e. O(1) space complexity, not O(n)*

*Do note that the space complexity can be O(n), only when you use some extra memory with n (variable, not fixed number) elements in it, like an array of n elements or a stack, etc (or sometimes also because of recursion due to implicit stack space), but here since you are only using a few variables (which are constant like every time you run the program it will have only fixed say 4 or 5 variables in it, it won't change from 4 to 6 or 7 depending upon the input provided, hence it is CONSTANT i.e. O(1) space.*



## Problem 5: Autocomplete with Tries

The idea of **suffixes()**: recurse down the trie, and connect the chars. If the node is the node of word, append a new item in the result list.

**insert()**: add new node if the char does not exist, and go down following the order of the word.

**find()**: following the order of the word and go down. If the char doesn't exist, return None. else, return the current node.

#### insert()

**Time Complexity**: O(n), n is the length of a word

**Space Complexity**: O(n), n is the length of a word

#### find()

**Time Complexity**: O(n), n is the length of a word

**Space Complexity**: Since the tries has been built already, no more memory used. O(1)

#### suffixes()

**Time Complexity**: O(m*n). m is the average length of a word, n is the number of words existing

**Space Complexity**: Since the tries has been built already, no more memory used. O(1)



## Problem 6: Max and Min in a Unsorted Array

Set the first element in the array is the max and min value. Go through the array and compare the items with the max and min value. If find value smaller than min value or bigger than max value, replace it.

**Time Complexity**: O(n)

**Space Complexity**: O(1)

*Since you are not using any extra/auxiliary space, here, it should be constant,i.e. O(1) space complexity, not O(n)*



## Problem 7: HTTPRouter using a Trie

When what to add a path or look up, first split path into a word list.

The class **RouteTrie** and **RouterTrieNode** are similar to the function in problem 5. The difference is that in the class **RouteTrieNode**, the variable is not is_word, but is is_handler. It will be used for saving the handler information. If the node is the end of a handler, it will be the handler name, otherwise it is "Not found handler".

The class **Router** is the main object in the problem. The variables in it include a object of RouteTrie. There are three main functions:

**split_path()**: used for split the path into several words and save in a word_list

**add_handler()**, add new node in the trie if the word doesn't exist. it use the insert function, similar to problem 5

**lookup():** call the function find() in the Trie, similar to problem 5.

#### add_handler()

**Time Complexity**: O(n)

**Space Complexity**: O(n)

#### look_up() 

**Time Complexity**: O(n)

**Space Complexity**: O(n)