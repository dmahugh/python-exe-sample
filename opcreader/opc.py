"""Tools for reading metadata from OPC packages"""
import xml.etree.cElementTree as ET
import zipfile


def get_content_types(fname):
    """Return content types as a dictionary.
    keys = part names
    values = content type for each part
    """
    tree = ET.fromstring(zipfile.ZipFile(fname).read("[Content_Types].xml"))

    content_types = dict()
    for elem in tree.iter():
        if "Extension" in elem.attrib:
            key = elem.attrib["Extension"]
            value = elem.attrib["ContentType"]
            content_types[key] = value
        elif "PartName" in elem.attrib:
            key = elem.attrib["PartName"]
            value = elem.attrib["ContentType"]
            content_types[key] = value

    return content_types


def get_parts(fname):
    """Returns a list of the parts in an OPC package.
    """
    with zipfile.ZipFile(fname) as zip_archive:
        parts = [name for name in zip_archive.namelist()]
    return sorted(parts)


def get_relationships(fname):
    """Return package relationships as a dictionary.
    keys = Relationship Id
    values = Relationship Type
    """
    tree = ET.fromstring(zipfile.ZipFile(fname).read("_rels/.rels"))

    relationships = dict()
    for elem in tree.iter():
        if "Id" in elem.attrib and "Type" in elem.attrib:
            key = elem.attrib["Id"]
            value = elem.attrib["Type"]
            relationships[key] = value

    return relationships
