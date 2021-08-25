def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 1:
        binary_search(input_list, number)

    left = 0
    right = len(input_list)
    mid = (right - left) // 2 + left

    if input_list[mid] == number:
        return mid

    if input_list[mid] > input_list[left]:
        left_result = binary_search(input_list[left:mid], number)
    else:
        left_result = rotated_array_search(input_list[left:mid], number)
    if input_list[mid] < input_list[right - 1]:
        right_result = binary_search(input_list[mid+1:right], number)
    else:
        right_result = rotated_array_search(input_list[mid+1:right], number)

    if left_result != -1:
        return left_result
    if right_result != -1:
        return right_result + mid + 1
    return -1


def binary_search(input_list, number):
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1
    if input_list[0] > number or input_list[-1] < number:
        return -1


    left = 0
    right = len(input_list)
    while right - left > 1:
        mid = (right - left) // 2 + left
        if input_list[mid] < number:
            left = mid + 1
        elif input_list[mid] > number:
            right = mid
        else:
            return mid
    if input_list[right] == number:
        return right
    if input_list[left] == number:
        return left
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print("Linear: {} || rotated: {}".format(linear_search(input_list, number), rotated_array_search(input_list, number)))
    # if linear_search(input_list, number) == rotated_array_search(input_list, number):
    #     print("Pass")
    # else:
    #     print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# test binary search
# print(binary_search([1,2,3,4,5,6],3))