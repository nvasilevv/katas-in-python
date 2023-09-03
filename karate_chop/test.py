import pytest
from main import chop, chop_recursive_wrapper, chop_array_recursive


@pytest.mark.parametrize(
    'number, array, expectation',
    [
        (3, [], -1),
        (3, [1], -1),
        (1, [1], 0),
        (1, [1, 3, 5], 0),
        (3, [1, 3, 5], 1),
        (5, [1, 3, 5], 2),
        (0, [1, 3, 5], -1),
        (2, [1, 3, 5], -1),
        (4, [1, 3, 5], -1),
        (6, [1, 3, 5], -1),
        (1, [1, 3, 5, 7], 0),
        (3, [1, 3, 5, 7], 1),
        (5, [1, 3, 5, 7], 2),
        (7, [1, 3, 5, 7], 3),
        (0, [1, 3, 5, 7], -1),
        (2, [1, 3, 5, 7], -1),
        (4, [1, 3, 5, 7], -1),
        (6, [1, 3, 5, 7], -1),
        (8, [1, 3, 5, 7], -1),
    ])
def test_chop(number, array, expectation):
    assert chop(number, array) == expectation


@pytest.mark.parametrize(
    'number, array, expectation',
    [
        (3, [], -1),
        (3, [1], -1),
        (1, [1], 0),
        (1, [1, 3, 5], 0),
        (3, [1, 3, 5], 1),
        (5, [1, 3, 5], 2),
        (0, [1, 3, 5], -1),
        (2, [1, 3, 5], -1),
        (4, [1, 3, 5], -1),
        (6, [1, 3, 5], -1),
        (1, [1, 3, 5, 7], 0),
        (3, [1, 3, 5, 7], 1),
        (5, [1, 3, 5, 7], 2),
        (7, [1, 3, 5, 7], 3),
        (0, [1, 3, 5, 7], -1),
        (2, [1, 3, 5, 7], -1),
        (4, [1, 3, 5, 7], -1),
        (6, [1, 3, 5, 7], -1),
        (8, [1, 3, 5, 7], -1),
    ])
def test_chop_recursive_wrapper(number, array, expectation):
    assert chop_recursive_wrapper(number, array) == expectation


@pytest.mark.parametrize(
    'number, array, expectation',
    [
        (3, [], -1),
        (3, [1], -1),
        (1, [1], 0),
        (1, [1, 3, 5], 0),
        (3, [1, 3, 5], 1),
        (5, [1, 3, 5], 2),
        (0, [1, 3, 5], -1),
        (2, [1, 3, 5], -1),
        (4, [1, 3, 5], -1),
        (6, [1, 3, 5], -1),
        (1, [1, 3, 5, 7], 0),
        (3, [1, 3, 5, 7], 1),
        (5, [1, 3, 5, 7], 2),
        (7, [1, 3, 5, 7], 3),
        (0, [1, 3, 5, 7], -1),
        (2, [1, 3, 5, 7], -1),
        (4, [1, 3, 5, 7], -1),
        (6, [1, 3, 5, 7], -1),
        (8, [1, 3, 5, 7], -1),
    ])
def test_chop_array_recursive(number, array, expectation):
    assert chop_array_recursive(number, array) == expectation
