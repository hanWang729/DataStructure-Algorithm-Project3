def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left_index = 0
    pivot_index = len(input_list) - 1
    pivot_index_2 = len(input_list) - 1
    pivot_value = 1

    while pivot_index_2 != left_index:
        i = input_list[left_index]
        if i < pivot_value:
            left_index += 1
        elif i > pivot_value:
            input_list[left_index] = input_list[pivot_index - 1]
            input_list[pivot_index - 1] = pivot_value
            input_list[pivot_index] = i
            pivot_index -= 1
            pivot_index_2 -= 1
        else:
            input_list[left_index] = input_list[pivot_index_2 - 1]
            input_list[pivot_index_2 - 1] = pivot_value
            input_list[pivot_index_2] = i
            pivot_index_2 -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 1])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 2])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1])