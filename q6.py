def find_first_negative(lst):
    """
    Finds the first negative number in a list using a while loop.
    Returns the first negative number, or "No negatives" if none are found.
    """

    # Check if lst is a list
    if type(lst) != list:
        return "Invalid input"

    index = 0  # Start from the first element

    # Loop through the list using while
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]  # Return the first negative number found
        index += 1

    # If no negative number is found
    return "No negatives"



# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)  # Output: -1

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)  # Output: "No negatives"

