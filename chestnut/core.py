from collections import namedtuple, defaultdict
import arrow
from chestnut.util import merge_tuples

__all__ = ['Author', 'authors',
           'histogram', 'YEAR', 'QUARTER', 'MONTH']


Author = namedtuple('Author', ('email', 'name', 'commit_count'))

# TODO: exclude merge commits


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


class BucketDivisor(object):
    @staticmethod
    def trim(ts):
        raise NotImplementedError

    @staticmethod
    def _next(date):
        raise NotImplementedError

    @classmethod
    def fill(cls, buckets):
        min_date = arrow.get(min(buckets.keys()))
        max_date = cls._next(arrow.get(max(buckets.keys())))

        dates = []
        date = min_date
        while date <= max_date:
            dates.append(date.timestamp)
            date = cls._next(date)

        return dates


class YearDivisor(BucketDivisor):
    @staticmethod
    def trim(ts):
        date = arrow.get(ts)
        new_date = date.floor('year')
        return new_date.timestamp

    @staticmethod
    def _next(date):
        return date.replace(years=+1)


class QuarterDivisor(BucketDivisor):
    @staticmethod
    def trim(ts):
        date = arrow.get(ts)
        trimmed_month = date.month - (date.month - 1) % 3
        new_date = date.replace(month=trimmed_month, day=1).floor('day')
        return new_date.timestamp

    @staticmethod
    def _next(date):
        return date.replace(months=+3)


class MonthDivisor(BucketDivisor):
    @staticmethod
    def trim(ts):
        date = arrow.get(ts)
        new_date = date.floor('month')
        return new_date.timestamp

    @staticmethod
    def _next(date):
        return date.replace(months=+1)


YEAR = YearDivisor
QUARTER = QuarterDivisor
MONTH = MonthDivisor


def histogram(commit_data, author=None, by=QUARTER):
    def is_author(author, email, name):
        return True

    buckets = defaultdict(set)
    for hex, email, name, ts in commit_data:
        if is_author(author, email, name):
            buckets[by.trim(ts)].add(hex)

    dates = by.fill(buckets)

    histogram = []
    for start, end in zip(dates[:-1], dates[1:]):
        histogram.append((start, end, len(buckets[start])))
    return histogram
