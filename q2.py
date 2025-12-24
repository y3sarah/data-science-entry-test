def find_and_replace(lst, find_val, replace_val):
    """
    This function finds all occurrences of find_val in a list
    and replaces them with replace_val.
    """

    # Check if lst is a list
    if type(lst) != list:
        return -1

    # Go through each index in the list
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    # Return the modified list
    return lst



# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)

