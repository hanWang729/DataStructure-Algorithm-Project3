def sort_all(input_list, begin_index, end_index):
    left_index = begin_index
    right_index = end_index
    pivot_index = right_index
    pivot_value = input_list[pivot_index]

    while pivot_index != left_index:
        i = input_list[left_index]
        if i >= pivot_value:
            left_index += 1
        else:
            input_list[left_index] = input_list[pivot_index - 1]
            input_list[pivot_index - 1] = pivot_value
            input_list[pivot_index] = i
            pivot_index -= 1
    return pivot_index


def sort_helper(input_list, begin_index, end_index):
    if end_index <= begin_index:
        return
    pivot_index = sort_all(input_list, begin_index, end_index)
    sort_helper(input_list, begin_index, pivot_index - 1)
    sort_helper(input_list, pivot_index + 1, end_index)


def quick_sort(input_list):
    sort_helper(input_list, 0, len(input_list) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quick_sort(input_list)
    result1 = ""
    result2 = ""
    for i in range(len(input_list)):
        if i % 2 == 0:
            result1 += str(input_list[i])
        else:
            result2 += str(input_list[i])
    return [int(result1), int(result2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
