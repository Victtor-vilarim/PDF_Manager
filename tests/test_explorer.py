import pytest

from modules import Explorer


def test_cd(tmp_path):
    sub = tmp_path / 'sub'
    sub.mkdir()

    ex = Explorer(root=tmp_path)
    ex.cd(sub)

    assert ex.wd == sub


def test_cd_two_dots(tmp_path):
    sub = tmp_path / 'sub'
    sub.mkdir()

    ex = Explorer(root=sub)

    ex.cd('..')

    assert ex.wd == tmp_path


def test_cd_error(tmp_path):
    ex = Explorer(root=tmp_path)

    with pytest.raises(FileNotFoundError):
        ex.cd('not_exist')


def test_cd_pos_error(tmp_path):
    ex = Explorer(root=tmp_path)

    with pytest.raises(FileNotFoundError):
        ex.cd('not_exist')

    assert ex.wd == tmp_path


def test_move(tmp_path):
    src = tmp_path / 'origin'
    src.mkdir()
    dst = tmp_path / 'destination'
    dst.mkdir()

    file_ = src / 'file.txt'
    file_.touch()

    ex = Explorer(root=src)

    ex.move(file_)

    ex.cd(dst)

    ex.to(file_)

    assert (dst / file_).exists()


def test_move_error(tmp_path):
    src = tmp_path / 'origin'
    src.mkdir()
    dst = tmp_path / 'destination'
    dst.mkdir()

    file_ = src / 'file.txt'

    ex = Explorer(root=src)

    with pytest.raises(FileNotFoundError):
        ex.move(file_)
