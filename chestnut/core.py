from collections import namedtuple, defaultdict
from chestnut.util import merge_tuples

__all__ = ['Author', 'authors']


Author = namedtuple('Author', ('email', 'name', 'commit_count'))


def authors(commit_data):
    commit_counter = defaultdict(set)
    for hex, email, name in commit_data:
        # TODO: check complexity of insert to python set
        commit_counter[(email, name)].add(hex)
    author_list = [Author(a[0], a[1], len(commits))
                   for a, commits in commit_counter.iteritems()]
    merged_author_list = merge_tuples(author_list, (0, 1), 2, Author)
    merged_author_list.sort(cmp=_cmp_authors)
    return merged_author_list


def _cmp_authors(x, y):
    cc_cmp = cmp(x.commit_count, y.commit_count)
    if cc_cmp != 0:
        return -cc_cmp
    else:
        return cmp(x.name, y.name)
