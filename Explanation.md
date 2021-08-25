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

**Space Complexity:** O(n)



## Problem 3: Rearrange Array Elements

1. Sort the array by quick sort
2. arrange the number in the array from the biggest to the smallest. give the number to two result one by one. then the sum is the maximum

**Time Complexity:** O(nlogn)

**Space Complexity**: O(n)



## Problem 4: Dutch National Flag Problem

This problem is similar to the idea of quick sort. Just use two pivot. if the number is 0, put it at the left of pivots, if 2, put it at the right of pivots, if 1 put it at the middle of pivots.

**Time Complexity:** O(n)

**Space Complexity:** O(n)



## Problem 5: Autocomplete with Tries

Just recurse down the trie, and connect the chars. If the node is the node of word, append a new item in the result list.

**Time Complexity (suffixes function)**: O(m*n). m is the average length of a word, n is the number of words existing

**Space Complexity (suffixes function)**: Since the tries has been built already, no more memory used. O(1)



## Problem 6: Max and Min in a Unsorted Array

Set the first element in the array is the max and min value. Go through the array and compare the items with the max and min value. If find value smaller than min value or bigger than max value, replace it.

**Time Complexity**: O(n)

**Space Complexity**: O(n)



## Problem 7: HTTPRouter using a Trie

When what to add a path or look up, first split path into a word list.

Other part is similar to problem 5.

#### add_handler()

**Time Complexity**: O(n)

**Space Complexity**: O(n)

#### look_up() 

**Time Complexity**: O(n)

**Space Complexity**: O(n)