import numpy
from helpers import _get_signed_areas, _near_equal

import meshzoo


def test_rectangle():
    points, cells = meshzoo.rectangle(nx=11, ny=11, variant="up")
    assert points.shape[1] == 121
    assert _near_equal(numpy.sum(points, axis=1), [60.5, 60.5])
    assert len(cells) == 200
    # assert numpy.all(_get_signed_areas(points, cells) > 0.0)

    points, cells = meshzoo.rectangle(nx=11, ny=11, variant="zigzag")
    assert points.shape[1] == 121
    assert _near_equal(numpy.sum(points, axis=1), [60.5, 60.5])
    assert len(cells) == 200

    points, cells = meshzoo.rectangle(nx=2, ny=2, variant="zigzag")
    assert points.shape[1] == 4
    assert _near_equal(numpy.sum(points, axis=1), [2.0, 2.0])
    assert len(cells) == 2

    points, cells = meshzoo.rectangle(nx=3, ny=2, variant="up")
    assert points.shape[1] == 6
    assert _near_equal(numpy.sum(points, axis=1), [3.0, 3.0])
    assert len(cells) == 4
    assert set(cells[0]) == {0, 1, 4}
    assert set(cells[2]) == {0, 3, 4}

    points, cells = meshzoo.rectangle(nx=3, ny=2, variant="zigzag")
    assert points.shape[1] == 6
    assert _near_equal(numpy.sum(points, axis=1), [3.0, 3.0])
    assert len(cells) == 4
    assert set(cells[0]) == {0, 1, 4}
    assert set(cells[2]) == {0, 3, 4}


def test_down():
    points, cells = meshzoo.rectangle(nx=5, ny=4, variant="down")
    assert points.shape[1] == 20
    assert len(cells) == 24
    # meshzoo.show2d(points, cells)


def test_center():
    points, cells = meshzoo.rectangle(nx=11, ny=9, variant="center")
    meshzoo.show2d(points, cells)
    assert points.shape[1] == 99
    assert len(cells) == 160


if __name__ == "__main__":
    test_center()
