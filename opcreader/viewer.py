"""Functions for displaying OPC metadata"""


def show_dict(dict2print, header):
    """Print a dictionary to the console.
    """
    if dict2print:
        width_column1 = max(map(len, dict2print.keys()))
        width_column2 = max(map(len, dict2print.values()))
        total_width = width_column1 + width_column2 + 1
    else:
        total_width = len(header) + 6
    show_str(header.center(total_width, "-"))
    for key, value in dict2print.items():
        print(str(key).ljust(width_column1) + " " + str(value).ljust(width_column2))


def show_list(list2print, header):
    """Print a list to the console.
    """
    if list2print:
        width = max(len(header) + 6, max(map(len, list2print)))
    else:
        width = len(header) + 6
    show_str(header.center(width, "-"))
    print("\n".join(sorted(list2print)))


def show_str(text):
    """Print a string to the console. Currently just a wrapper for print().
    """
    print(text)
