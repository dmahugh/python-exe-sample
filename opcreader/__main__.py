"""Command line too for reading metadata and structure of OPC package

Usage: opcinfo <options> filename

Options:
  -c, --content_types    Show content types. (default option)
  -r, --relationships    Show package relationships.
  -s, --structure        Show ZIP archive structure.
  -h, --help             Show help screen only (this message).

See https://github.com/dmahugh/python-exe-sample for more information
"""
import pprint
import sys

from opcreader import get_content_types
from opcreader import viewer


def main():
    """main entry point for CLI"""

    arguments = [_ for _ in sys.argv[1:] if not _.startswith("-")]
    options = [_ for _ in sys.argv[1:] if _.startswith("-")]

    if "-h" in options or "--help" in options:
        viewer.show(__doc__)  # show help screen
        return

    # validate arguments
    if len(arguments) != 1:
        viewer.show("Wrong number of filename arguments!")
        return
    filename = arguments[0]

    # validate options
    valid_options = [
        "-c",
        "--content_types",
        "-r",
        "--relationships",
        "-s",
        "--structure",
        "-h",
        "--help",
    ]
    invalid_options = [option for option in options if option not in valid_options]
    if invalid_options:
        viewer.show(f"Invalid options: {invalid_options}")
        return

    if "-c" in options or "--content_types" in options or not options:
        content_types = get_content_types(filename)
        viewer.show(f"Content types:\n{pprint.pformat(content_types)}")

    if "-r" in options or "--relationships" in options:
        viewer.show(f"/// relationships for {filename}")

    if "-s" in options or "--structure" in options:
        viewer.show(f"/// structure for {filename}")


if __name__ == "__main__":
    main()
