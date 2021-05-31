# without taking any more space

# Gap Method


def merge(arr1, arr2, n, m):
    # if m > n:
    #     arr1, arr2 = arr2, arr1
    #     m, n = n, m

    gap = (m + n) // 2 + (m + n) % 2

    while gap > 0:

        # just for arr1
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]

            i += 1

        # just for arr1 and arr2
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]

            i += 1
            j += 1

        # just for arr2
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = gap // 2 + gap % 2
        if gap == 1:
            gap = 0

if __name__ == "__main__":

    a2 = [10, 27, 38, 43, 82]
    a1 = [3, 9]
    n = len(a1)
    m = len(a2)

        # Function Call
    merge(a1, a2, n, m)

    print("First Array: ", end="")
    for i in range(n):
        print(a1[i], end=" ")
    print()

    print("Second Array: ", end="")
    for i in range(m):
        print(a2[i], end=" ")
    print()
