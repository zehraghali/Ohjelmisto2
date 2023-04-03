def even(arr):
    result = []
    for num in arr:
        if num % 2 == 0:
            result.append(num)
    return result
arr = [2, 7, 4]
result = even(arr)
print("Original array:", arr)
print("New array:", result)
