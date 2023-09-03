import pytest
from main import convert_to_roman


@pytest.mark.parametrize('number, expectation', [
    (0, ""),
    (1, 'I'),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (9, 'IX'),
    (10, 'X'), 
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'), 
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M'),
    (2024, "MMXXIV")
])
def test_convert_to_roman(number, expectation):
    assert convert_to_roman(number) == expectation
