"""content_types.py"""
import json
import sys
import xml.etree.cElementTree as ET
import zipfile

def print_content_types(fname):
    """Open an OPC document and print the content types to the console"""
    tree = ET.fromstring(zipfile.ZipFile(fname).read('[Content_Types].xml'))
    content_types = \
        [dict(PartName=elem.attrib['PartName'],
              ContentType=elem.attrib['ContentType'])
         for elem in tree.iter()
         if 'PartName' in elem.attrib and 'ContentType' in elem.attrib]
    print(json.dumps(content_types, indent=4, sort_keys=True))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_content_types(sys.argv[1])
    else:
        print('SYNTAX: python content_types.py filename')
