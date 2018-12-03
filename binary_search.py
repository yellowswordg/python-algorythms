# Binary search will only work with sorted array.
# Worst-case performance	O(log n)
# Best-case performance	O(1)
# Average performance	O(log n)
# Worst-case space complexity

def binary_search(arr ,item):
    first = 0
    last = len(arr)-1

    while first <=last:
        mid = (first + last)//2
        guess = arr[mid]
        if guess == item:
            return f"found in index {mid}"
        if guess > item:
            last = mid - 1
        else:
            first = mid + 1
    return "Nothing in this list"

my_list = [1, 2, 4, 5, 7, 8, 9, 12, 22, 33, 44, 55, 6]
print(binary_search(my_list, 12))