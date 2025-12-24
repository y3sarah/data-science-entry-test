def update_dictionary(dct, key, value):
    """
    Updates a dictionary with a key-value pair.
    Prints a message whether the key is new or existing.
    Returns the updated dictionary.
    """

    if key in dct:
        print(f"The key '{key}' already exists with value: {dct[key]}")
    else:
        print(f"Adding new key '{key}' with value: {value}")

    # Update the dictionary
    dct[key] = value

    # Return the updated dictionary
    return dct



# Scenario 1: empty dictionary
result1 = update_dictionary({}, "name", "Alice")
print(result1)
# Output:
# Adding new key 'name' with value: Alice
# {'name': 'Alice'}

# Scenario 2: key already exists
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
# Output:
# The key 'age' already exists with value: 25
# {'age': 26}

