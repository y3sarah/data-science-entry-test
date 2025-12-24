def string_reverse(s):
    """
    This function reverses a given string using a loop.
    If s is not a string, it returns -1.
    """

    # Check if input is a string
    if type(s) != str:
        return -1

    # Start with an empty string for the reversed result
    reversed_s = ""

    # Loop through each character in the string from end to start
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]  # Add each character to the reversed string

    # Return the reversed string
    return reversed_s



# Scenario 1
result1 = string_reverse("Hello World")
print(result1)  # Output: "dlroW olleH"

# Scenario 2
result2 = string_reverse("Python")
print(result2)  # Output: "nohtyP"
