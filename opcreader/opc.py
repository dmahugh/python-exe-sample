"""Tools for reading metadata from OPC packages"""
import json
import sys
import xml.etree.cElementTree as ET
import zipfile


def get_content_types(fname):
    """Return content types as a dict.
    """
    tree = ET.fromstring(zipfile.ZipFile(fname).read("[Content_Types].xml"))
    content_types = [
        dict(PartName=elem.attrib["PartName"], ContentType=elem.attrib["ContentType"])
        for elem in tree.iter()
        if "PartName" in elem.attrib and "ContentType" in elem.attrib
    ]
    return content_types
