from chestnut.core import histogram, QUARTER, MONTH, YEAR
import arrow
import pytest


@pytest.mark.parametrize('divisor,expected', [
    (YEAR, [
        (arrow.get(2014, 1, 1).timestamp,
         arrow.get(2015, 1, 1).timestamp, 1),
        (arrow.get(2015, 1, 1).timestamp,
         arrow.get(2016, 1, 1).timestamp, 2),
    ]),
    (QUARTER, [
        (arrow.get(2014, 10, 1).timestamp,
         arrow.get(2015, 1, 1).timestamp, 1),
        (arrow.get(2015, 1, 1).timestamp,
         arrow.get(2015, 4, 1).timestamp, 0),
        (arrow.get(2015, 4, 1).timestamp,
         arrow.get(2015, 7, 1).timestamp, 2),
    ]),
    (MONTH, [
        (arrow.get(2014, 12, 1).timestamp,
         arrow.get(2015, 1, 1).timestamp, 1),
        (arrow.get(2015, 1, 1).timestamp,
         arrow.get(2015, 2, 1).timestamp, 0),
        (arrow.get(2015, 2, 1).timestamp,
         arrow.get(2015, 3, 1).timestamp, 0),
        (arrow.get(2015, 3, 1).timestamp,
         arrow.get(2015, 4, 1).timestamp, 0),
        (arrow.get(2015, 4, 1).timestamp,
         arrow.get(2015, 5, 1).timestamp, 0),
        (arrow.get(2015, 5, 1).timestamp,
         arrow.get(2015, 6, 1).timestamp, 2),
    ]),
])
def test_histogram_divisor(divisor, expected):
    data = [('f644aa1ac062df528bf27b3d9f444960da7d8245',
             'j.doe@gmail.com', 'John Doe',
             arrow.get(2014, 12, 27).timestamp),
            ('d78c4c0c506a33ef958d6a15d1ea653d83f09e40',
             'j.doe@gmail.com', 'John Doe',
             arrow.get(2015, 5, 2).timestamp),
            ('34f876266b9ed09f788417262b8e1599b6098051',
             'j.doe@gmail.com', 'John Doe',
             arrow.get(2015, 5, 3).timestamp)]
    assert histogram(data, by=divisor) == expected

