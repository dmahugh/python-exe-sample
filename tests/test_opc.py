"""Tests for the opcreader.opc module"""
import os.path

import pytest

from opcreader import get_content_types, get_relationships, get_structure

CURRENT_FOLDER = os.path.dirname(__file__)


def test_get_content_types_docx():
    """Test reading content types from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.docx")
    expected = {
        "rels": "application/vnd.openxmlformats-package.relationships+xml",
        "xml": "application/xml",
        "/word/document.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
        "/word/styles.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
        "/word/settings.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
        "/word/webSettings.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
        "/word/fontTable.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
        "/word/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
        "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
        "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
        "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
    }
    assert get_content_types(filename) == expected


def test_get_content_types_xlsx():
    """Test reading content types from an XLSX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.xlsx")
    expected = {
        "rels": "application/vnd.openxmlformats-package.relationships+xml",
        "xml": "application/xml",
        "/xl/workbook.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
        "/xl/worksheets/sheet1.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
        "/xl/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
        "/xl/styles.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
        "/xl/sharedStrings.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
        "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
        "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
        "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
    }
    assert get_content_types(filename) == expected


def test_get_content_types_pptx():
    """Test reading content types from a PPTX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.pptx")
    expected = {
        "jpeg": "image/jpeg",
        "rels": "application/vnd.openxmlformats-package.relationships+xml",
        "xml": "application/xml",
        "/ppt/presentation.xml": "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
        "/ppt/slideMasters/slideMaster1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
        "/ppt/slides/slide1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slide+xml",
        "/ppt/presProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
        "/ppt/viewProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
        "/ppt/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
        "/ppt/tableStyles.xml": "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
        "/ppt/slideLayouts/slideLayout1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout2.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout3.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout4.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout5.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout6.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout7.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout8.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout9.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout10.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/ppt/slideLayouts/slideLayout11.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
        "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
        "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
        "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
    }
    assert get_content_types(filename) == expected


def test_get_relationships_docx():
    """Test reading relationships from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.docx")
    expected = {
        "rId3": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
        "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
        "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
        "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
    }
    assert get_relationships(filename) == expected


def test_get_relationships_xlsx():
    """Test reading relationships from a XLSX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.xlsx")
    expected = {
        "rId3": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
        "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
        "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
        "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
    }
    assert get_relationships(filename) == expected


def test_get_relationships_pptx():
    """Test reading relationships from a PPTX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdata.pptx")
    expected = {
        "rId3": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
        "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail",
        "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
        "rId5": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
        "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
    }
    assert get_relationships(filename) == expected
