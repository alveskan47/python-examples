def remove_duplicates(list):
    unique_items = []
    for item in list:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items
print(remove_duplicates([1, 2, 2, 1, 3, 3, 4, 5]))