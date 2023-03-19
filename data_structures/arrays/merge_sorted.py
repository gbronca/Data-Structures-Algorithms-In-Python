"""Merge two arrays into one sorted array"""


def merge_sorted(a: list, b: list = None) -> list:
    """Merge two arrays into one sorted array"""

    # Python easiest way to merge and sort 2 lists
    # return sorted(a + b)

    if b is None:
        b = []

    if not a or not b:
        return a + b

    merged_list = []
    i = 0
    j = 0

    while i < len(a) or j < len(b):
        if a[i] <= b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
        if i == len(a):
            merged_list.extend(b[j:])
            return merged_list
        if j == len(b):
            merged_list.extend(a[i:])
            return merged_list


sorted_list = merge_sorted([5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5])
print(sorted_list)
