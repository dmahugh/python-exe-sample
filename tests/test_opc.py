"""Tests for the opcreader.opc module"""
import os.path

# For readability, expected test results are stored in a separate constants.py
# file, because they're long and messy.
import constants

from opcreader import get_content_types, get_parts, get_relationships

CURRENT_FOLDER = os.path.dirname(__file__)


def test_get_content_types_docx():
    """Test reading content types from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.docx")
    assert get_content_types(filename) == constants.DOCX_CONTENT_TYPES

def test_get_content_types_pptx():
    """Test reading content types from a PPTX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.pptx")
    assert get_content_types(filename) == constants.PPTX_CONTENT_TYPES

def test_get_content_types_xlsx():
    """Test reading content types from an XLSX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.xlsx")
    assert get_content_types(filename) == constants.XLSX_CONTENT_TYPES

def test_get_parts_docx():
    """Test reading part names from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.docx")
    assert get_parts(filename) == constants.DOCX_PARTS

def test_get_parts_pptx():
    """Test reading part names from a PPTX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.pptx")
    assert get_parts(filename) == constants.PPTX_PARTS

def test_get_parts_xlsx():
    """Test reading part names from a XLSX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.xlsx")
    assert get_parts(filename) == constants.XLSX_PARTS

def test_get_relationships_docx():
    """Test reading relationships from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.docx")
    assert get_relationships(filename) == constants.DOCX_RELATIONSHIPS

def test_get_relationships_pptx():
    """Test reading relationships from a PPTX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.pptx")
    assert get_relationships(filename) == constants.PPTX_RELATIONSHIPS

def test_get_relationships_xlsx():
    """Test reading relationships from a XLSX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.xlsx")
    assert get_relationships(filename) == constants.XLSX_RELATIONSHIPS
