movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gillman", 91,
    [
        "Graham Chapman",
        [
            "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"
        ]
    ]
]

def print_lol(the_list):
    for list_item in the_list:
        if isinstance(list_item,list):
            print(len(list_item))
            print_lol(list_item)
        else:
            print(list_item)


print_lol(movies)