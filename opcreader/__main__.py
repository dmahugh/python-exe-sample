"""Command line too for reading metadata and structure of OPC package

Usage: opcinfo <options> filename

Options:
  -c, --content_types    Show content types. (default option)
  -p, --parts            Show part names.
  -r, --relationships    Show package relationships.
  -h, --help             Show help screen only (this message).

See https://github.com/dmahugh/python-exe-sample for more information
"""
import sys

from opcreader import get_content_types, get_parts, get_relationships
from opcreader import viewer


def main():
    """main entry point for CLI"""
    arguments = [_ for _ in sys.argv[1:] if not _.startswith("-")]
    options = [_ for _ in sys.argv[1:] if _.startswith("-")]

    if "-h" in options or "--help" in options:
        viewer.show_str(__doc__)  # show help screen
        return

    # validate arguments
    if len(arguments) != 1:
        viewer.show_str("Wrong number of filename arguments!")
        return
    filename = arguments[0]

    # validate options
    valid_options = [
        "-c",
        "--content_types",
        "-p",
        "--parts",
        "-r",
        "--relationships",
        "-h",
        "--help",
    ]
    invalid_options = [option for option in options if option not in valid_options]
    if invalid_options:
        viewer.show_str(f"Invalid options: {invalid_options}")
        return

    for option in options:
        if option in ["-c", "--content_types"]:
            content_types = get_content_types(filename)
            viewer.show_dict(content_types, "Content types:")
        if option in ["-r", "--relationships"]:
            relationships = get_relationships(filename)
            viewer.show_dict(relationships, "Relationships:")
        if option in ["-p", "--parts"]:
            parts = get_parts(filename)
            viewer.show_list(parts, "Part names:")


if __name__ == "__main__":
    main()
