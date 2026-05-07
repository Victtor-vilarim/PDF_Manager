import pytest

from pdf_manager.modules import Console


def test_help():
    assert Console().help('exit') != ''


def test_help_error():
    with pytest.raises(NotImplementedError):
        Console().help('root')
