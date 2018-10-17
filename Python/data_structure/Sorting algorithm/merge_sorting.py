
#合并排序


def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array

numbers = [6,5,3,7,2,8,4]
print(quick_sort(numbers))