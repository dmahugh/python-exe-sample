"""Tests for the opcreader.opc module"""
import os.path

import pytest

# For readability, expected test results are stored in a separate testdata.py
# file, because they're long and messy.
import testdata

from opcreader import get_content_types, get_parts, get_relationships

CURRENT_FOLDER = os.path.dirname(__file__)


@pytest.mark.parametrize(
    "filetype,expected",
    [
        ("docx", testdata.DOCX_CONTENT_TYPES),
        ("pptx", testdata.PPTX_CONTENT_TYPES),
        ("xlsx", testdata.XLSX_CONTENT_TYPES),
    ],
)
def test_get_content_types(filetype, expected):
    """Test get_content_types() with various OPC file types.
    """
    filename = os.path.join(CURRENT_FOLDER, f"testdata.{filetype}")
    assert get_content_types(filename) == expected


@pytest.mark.parametrize(
    "filetype,expected",
    [
        ("docx", testdata.DOCX_PARTS),
        ("pptx", testdata.PPTX_PARTS),
        ("xlsx", testdata.XLSX_PARTS),
    ],
)
def test_get_parts(filetype, expected):
    """Test get_parts() with various OPC file types.
    """
    filename = os.path.join(CURRENT_FOLDER, f"testdata.{filetype}")
    assert get_parts(filename) == expected


@pytest.mark.parametrize(
    "filetype,expected",
    [
        ("docx", testdata.DOCX_RELATIONSHIPS),
        ("pptx", testdata.PPTX_RELATIONSHIPS),
        ("xlsx", testdata.XLSX_RELATIONSHIPS),
    ],
)
def test_get_relationships(filetype, expected):
    """Test get_relationships() with various OPC file types.
    """
    filename = os.path.join(CURRENT_FOLDER, f"testdata.{filetype}")
    assert get_relationships(filename) == expected
