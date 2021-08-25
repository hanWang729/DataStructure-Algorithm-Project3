def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None:
        return []
    if len(ints) == 0:
        return []
    min_value = ints[0]
    max_value = ints[0]
    for i in ints:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    result = (min_value, max_value)
    return result



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Test 1: normal test
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test 2: empty input
print(get_min_max([])) # []

# Test 3: None input
print(get_min_max(None)) # []