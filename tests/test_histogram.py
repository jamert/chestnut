from chestnut.core import histogram


def test_histogram_basic():
    data = [('f644aa1ac062df528bf27b3d9f444960da7d8245',
             'j.doe@gmail.com', 'John Doe', 1420071345L),
            ('d78c4c0c506a33ef958d6a15d1ea653d83f09e40',
             'j.doe@gmail.com', 'John Doe', 1427846400L),
            ('34f876266b9ed09f788417262b8e1599b6098051',
             'j.doe@gmail.com', 'John Doe', 1435708755)]
    result = [
        (1420070400, 1427846400, 1),
        (1427846400, 1435708800, 2),
    ]
    assert histogram(data, by='quarter') == result
