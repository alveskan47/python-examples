def count_occurrences(list, target):
    count = 0
    for index in range(0, len(list)):
        if list[index] == target:
            count += 1
    return count

print(count_occurrences([5, 2, 3, 5, 5, 4, 2], 5))