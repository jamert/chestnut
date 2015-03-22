from collections import namedtuple, defaultdict
import arrow
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
    # TODO: use found merges to other functions (possibly)
    merged_author_list = merge_tuples(author_list, (0, 1), 2, Author)
    merged_author_list.sort(cmp=_cmp_authors)
    return merged_author_list


def _cmp_authors(x, y):
    cc_cmp = cmp(x.commit_count, y.commit_count)
    if cc_cmp != 0:
        return -cc_cmp
    else:
        return cmp(x.name, y.name)


def histogram(commit_data, author=None, by='quarter'):
    def trim_timestamp(ts):
        date = arrow.get(ts)
        print date
        trimmed_month = date.month - (date.month - 1) % 3
        new_date = date.replace(month=trimmed_month, day=1).floor('day')
        print new_date
        return new_date.timestamp

    def next_date(date):
        return date.replace(months=+3)

    def is_author(author, email, name):
        return True

    buckets = defaultdict(set)
    for hex, email, name, ts in commit_data:
        if is_author(author, email, name):
            buckets[trim_timestamp(ts)].add(hex)

    min_date = arrow.get(min(buckets.keys()))
    max_date = arrow.get(max(buckets.keys())).replace(months=+3)
    dates = []
    date = min_date
    while date <= max_date:
        dates.append(date.timestamp)
        date = next_date(date)

    histogram = []
    for start, end in zip(dates[:-1], dates[1:]):
        histogram.append((start, end, len(buckets[start])))
    return histogram
