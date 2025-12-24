def swap(x, y):
    """
    This function swaps the values of x and y.
    If x or y is not a number, it returns -1.
    """

    # Check if x is NOT a number
    if type(x) != int and type(x) != float:
        return -1

    # Check if y is NOT a number
    if type(y) != int and type(y) != float:
        return -1

    # Store x in a temporary variable
    temp = x

    # Assign y to x
    x = y

    # Assign temp (old x) to y
    y = temp

    # Print the swapped values
    print("x:", x)
    print("y:", y)



# Scenario 1
result = swap("Apple", 10)
print(result)   # Output: -1

# Scenario 2
swap(9, 17)     # Output: x: 17, y: 9
