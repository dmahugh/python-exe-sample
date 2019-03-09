"""Tests for opcreader.viewer"""
import pytest

from opcreader import viewer

def test_show(capsys):
    """Test that show adds information to stdout
    /// TO DO: replace this RealPython sample test with our test
    """
    text = "Lorem ipsum dolor sit amet"
    viewer.show(text)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""

    # It's ok if the viewer adds some information
    assert text in stdout
