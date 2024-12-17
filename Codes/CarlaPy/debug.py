def print_function_names(obj):
    # Get the list of all attributes of the object
    attributes = dir(obj)
    # Filter out the function names
    function_names = [name for name in attributes if callable(getattr(obj, name))]
    # Print the function names
    for name in function_names:
        print(name)

def print_all_attributes(obj):
    # Get the list of all attributes of the object
    attributes = dir(obj)
    # Print all attributes and their values
    for attr_name in attributes:
        attr_value = getattr(obj, attr_name)
        print(f"{attr_name}: {attr_value}")

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def print_list(lst):
    for item in lst:
        print(item)


def get_key_from_value(dictionary, value, log=False):
    for key, val in dictionary.items():
        if val == value:
            log and print(f"The key corresponding to value {value} is: {key}")
            return key
    log and print(f"No key found for value {value}")
    return None  # Value not found in the dictionary