def check_divisibility(num, divisor):
    """
    Checks if num is divisible by divisor.
    Returns True if divisible, False if not.
    Returns -1 if either input is not numeric.
    """

    # Check if both inputs are numbers
    if type(num) != int and type(num) != float:
        return -1
    if type(divisor) != int and type(divisor) != float:
        return -1

    # Avoid division by zero
    if divisor == 0:
        print("Cannot divide by zero!")
        return False

    # Check divisibility
    if num % divisor == 0:
        return True
    else:
        return False



# Scenario 1
result1 = check_divisibility(10, 2)
print(result1)  # Output: True

# Scenario 2
result2 = check_divisibility(7, 3)
print(result2)  # Output: False
