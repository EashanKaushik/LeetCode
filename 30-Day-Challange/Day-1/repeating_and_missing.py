# can solve using count array as well

def repeat_and_missing(arr, size):

    for index in range(0, size):
        if arr[abs(arr[index]) - 1] > 0:
            arr[abs(arr[index]) - 1] = -arr[abs(arr[index]) - 1]
        else:
            repeat = abs(arr[index])

    missing = arr.index(max(arr)) + 1

    return missing, repeat


print(repeat_and_missing([4, 3, 6, 2, 1, 1], 6))
