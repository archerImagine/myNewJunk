"""
This is the nester.py module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists.
"""
def print_lol(the_list):
    """
    This function takes a positional argument called "the_list", which is any
    Python list(of, possibly, nested list). Each data item in the provided list is
    (recursively) printed to the screen on its own line.
    :param the_list:
    :return: prints the list
    """
    for list_item in the_list:
        if isinstance(list_item,list):
            print(len(list_item))
            print_lol(list_item)
        else:
            print(list_item)