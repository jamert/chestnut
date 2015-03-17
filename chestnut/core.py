from collections import namedtuple, defaultdict

__all__ = ['Author', 'authors']


Author = namedtuple('Author', ('email', 'name', 'commit_count'))


def authors(commit_data):
    commit_counter = defaultdict(set)
    for hex, email, name in commit_data:
        # TODO: check complexity of insert to python set
        commit_counter[(email, name)].add(hex)
    author_list = [Author(a[0], a[1], len(commits))
                   for a, commits in commit_counter.iteritems()]
    author_list.sort(key=lambda a: a.commit_count, reverse=True)
    return author_list
