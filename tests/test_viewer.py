"""Tests for opcreader.viewer"""
from opcreader import viewer


def test_show_dict(capsys):
    """Test that show_dict() writes expected output.
    """
    expected = "---------header--------\n" + \
        "key1       value1      \nkey2       value2      \nlonger_key longer_value"
    viewer.show_dict(
        {"key1": "value1", "key2": "value2", "longer_key": "longer_value"}, "header"
    )
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert expected in stdout


def test_show_dict_empty(capsys):
    """Test that show_dict() writes expected output when dict is empty.
    """
    expected = 6 * "-"
    viewer.show_dict({}, "")
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert expected in stdout


def test_show_list(capsys):
    """Test that show_list() writes expected output.
    """
    expected = "---header---\nstring1\nstring2\nstring3"
    viewer.show_list(["string1", "string2", "string3"], "header")
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert expected in stdout


def test_show_list_empty(capsys):
    """Test that show_list() writes expected output when list is empty.
    """
    expected = 6 * "-"
    viewer.show_list([], "")
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert expected in stdout


def test_show_str(capsys):
    """Test that show_str() writes to stdout
    """
    text = "This string should appear in stdout."
    viewer.show_str(text)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert text in stdout
