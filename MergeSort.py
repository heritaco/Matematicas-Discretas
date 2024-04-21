def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage:
arr = [5, 2, 8, 12, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# The loop invariant for the while loop inside the merge function is that at the start of each iteration, the merged list contains the sorted elements from the initial segments of the left and right lists. More specifically, it contains the smallest elements from the combined initial segments of left and right that have been seen so far, and these elements are in sorted order.
# This invariant is established before the loop starts (since merged is initially empty and there are no initial segments of left and right), and each iteration of the loop maintains the invariant by appending the smallest unseen element from left or right to merged.
