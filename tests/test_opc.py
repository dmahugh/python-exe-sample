"""Tests for the opcreader.opc module"""
import os.path

import pytest

from opcreader import get_content_types

CURRENT_FOLDER = os.path.dirname(__file__)


def test_get_content_types_docx():
    """Test reading content types from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdocs/simpletest.docx")
    expected = [
        {
            "PartName": "/word/document.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
        },
        {
            "PartName": "/word/styles.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
        },
        {
            "PartName": "/word/settings.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
        },
        {
            "PartName": "/word/webSettings.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
        },
        {
            "PartName": "/word/fontTable.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
        },
        {
            "PartName": "/word/theme/theme1.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.theme+xml",
        },
        {
            "PartName": "/docProps/core.xml",
            "ContentType": "application/vnd.openxmlformats-package.core-properties+xml",
        },
        {
            "PartName": "/docProps/app.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
        },
        {
            "PartName": "/docProps/custom.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
        },
    ]

    assert get_content_types(filename) == expected
