from chestnut.repository import Repository


def test_repository_commit_data():
    repo = Repository('tests/data/testrepo.git')
    data = set((
        ('8bed03360e9227ab20cf2a086a8a14ee2a30b7fd',
         'dayneko.ab@gmail.com', 'Artem Dayneko'),
        ('79281dde8e84fa10d3eaedd415e9a920e4abf507',
         'dayneko.ab@gmail.com', 'Artem Dayneko'),
        ('056e626e51b1fc1ee2182800e399ed8d84c8f082',
         'xavier.delannoy@gmail.com', 'delanne'),
        ('ccca47fbb26183e71a7a46d165299b84e2e6c0b3',
         'xavier.delannoy@gmail.com', 'delanne'),
        ('2cdae28389c059815e951d0bb9eed6533f61a46b',
         'p.hosek@imperial.ac.uk', 'Petr Hosek'),
        ('5fe808e8953c12735680c257f56600cb0de44b10',
         'dborowitz@google.com', 'Dave Borowitz'),
        ('c2792cfa289ae6321ecf2cd5806c2194b0fd070c',
         'dborowitz@google.com', 'Dave Borowitz'),
        ('784855caf26449a1914d2cf62d12b9374d76ae78',
         'Nico.Geyso@FU-Berlin.de', 'Nico von Geyso'),
        ('f5e5aa4e36ab0fe62ee1ccc6eb8f79b866863b87',
         'Nico.Geyso@FU-Berlin.de', 'Nico von Geyso'),
    ))
    assert set(repo.commit_data) == data
