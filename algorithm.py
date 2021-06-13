def canBeSplitted(arr):
    length_arr = len(arr)

    if length_arr == 0:
        return 0
    
    for i in range(length_arr):
        if i > 0:
            left_sum = sum(arr[:i])
            right_sum = sum(arr[i:])

            if left_sum == right_sum:
                return 1

    return -1


if __name__ == '__main__':
    assert canBeSplitted([]) == 0
    assert canBeSplitted([1]) == -1
    assert canBeSplitted([1, 2, 1]) == -1
    assert canBeSplitted([1, 3, 3, 8, 4, 3, 2, 3, 3]) == 1
