import random


def quick_select(arr, k_index):
    # Checking if an array has at least one element
    if len(arr) == 1:
        return arr[0]

    # Picking a random pivot
    pivot = random.choice(arr)

    # Splitting an array into three parts
    lows = [x for x in arr if x < pivot]  # Lower than pivot
    equals = [x for x in arr if x == pivot]  # Equal to pivot
    highs = [x for x in arr if x > pivot]  # Higher than за pivot

    # Seeking k-th element
    if k_index <= len(lows):
        return quick_select(lows, k_index)  # In the left part
    elif k_index <= len(lows) + len(equals):
        return pivot  # Pivot is the answer
    else:
        return quick_select(highs, k_index - len(lows) - len(equals))  # In the right part


def ordinal_suffix(k_index):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return suffixes.get(k_index % 10, 'th') if not 10 <= k_index % 100 <= 20 else 'th'


# Generating a list of 10 random integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print(f"Initial array: {random_list}")
k = random.randint(1, 10)


kth_smallest = quick_select(random_list, k)
print(f"{k}{ordinal_suffix(k)} smallest element: {kth_smallest}")
