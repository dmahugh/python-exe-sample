"""Read metadata from an OPC package
See https://github.com/dmahugh/python-exe-sample

Command line usage: opcinfo filename
"""
import sys

from opcreader import get_content_types
from opcreader import viewer

def main():
    """main entry point"""

    # get arguments and options from command line
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # handle help command
    if "-h" in opts or "--help" in opts:
        viewer.show(__doc__)
        return

    viewer.show("Hello world from opcreader!")


if __name__ == "__main__":
    main()
