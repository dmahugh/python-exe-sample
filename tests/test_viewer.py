"""Tests for opcreader.viewer"""
import pytest

from opcreader import viewer

def test_show(capsys):
    """Test that show() writes to stdout
    """
    text = "Lorem ipsum dolor sit amet"
    viewer.show(text)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
