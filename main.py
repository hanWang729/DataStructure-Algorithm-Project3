# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def sort_all(input_list, begin_index, end_index):
    left_index = begin_index
    right_index = end_index
    pivot_index = right_index
    pivot_value = input_list[pivot_index]

    while pivot_index != left_index:
        i = input_list[left_index]
        if i <= pivot_value:
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


def solution(A):
    # write your code in Python 3.6
    quick_sort(A)
    print(A)
    smallest_value = 1
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        if A[i] == smallest_value:
            smallest_value += 1
        elif A[i] > smallest_value:
            return smallest_value
    return smallest_value + 1


print(solution([1,2,3]))