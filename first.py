import random

# Generating a list of 10 random integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print(f"Initial array: {random_list}")


def divide_and_conquer(arr):
    # Basic case: one element
    if len(arr) == 1:
        return arr[0], arr[0]

    # Basic case: two elements
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    # Splitting an array into two parts
    mid = len(arr) // 2
    left_min, left_max = divide_and_conquer(arr[:mid])
    right_min, right_max = divide_and_conquer(arr[mid:])

    # Combining results
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max


# Usage example
result = divide_and_conquer(random_list)
print("Min:", result[0])
print("Max:", result[1])
