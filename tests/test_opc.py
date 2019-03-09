"""Tests for the opcreader.opc module"""
import os.path

import pytest

from opcreader import get_content_types

CURRENT_FOLDER = os.path.dirname(__file__)


def test_get_content_types_docx():
    """Test reading content types from a DOCX file"""
    filename = os.path.join(CURRENT_FOLDER, "testdocs/simpletest.docx")
    expected = {
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
