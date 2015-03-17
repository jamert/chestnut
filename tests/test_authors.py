from chestnut.core import authors, Author


def test_authors_counter():
    data = [('f644aa1ac062df528bf27b3d9f444960da7d8245',
             'j.doe@mail.com', 'John'),
            ('d78c4c0c506a33ef958d6a15d1ea653d83f09e40',
             'j.doe@mail.com', 'John'),
            ('34f876266b9ed09f788417262b8e1599b6098051',
             'm.dowell@mail.com', 'Mary')]
    assert authors(data) == [Author('j.doe@mail.com', 'John', 2),
                             Author('m.dowell@mail.com', 'Mary', 1)]


def test_authors_repeating():
    data = [('f644aa1ac062df528bf27b3d9f444960da7d8245',
             'j.doe@mail.com', 'John'),
            ('d78c4c0c506a33ef958d6a15d1ea653d83f09e40',
             'j.doe@mail.com', 'John'),
            ('d78c4c0c506a33ef958d6a15d1ea653d83f09e40',
             'j.doe@mail.com', 'John')]
    assert authors(data) == [Author('j.doe@mail.com', 'John', 2)]
