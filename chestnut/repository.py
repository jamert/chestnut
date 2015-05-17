import pygit2
from .core import authors, \
    histogram as core_histogram, \
    YEAR, QUARTER, MONTH


class Repository(object):
    def __init__(self, path):
        self._repo = pygit2.Repository(path)
        self._commit_data = None

    @property
    def commit_data(self):
        if not self._commit_data:
            self._load_commit_data()
        return self._commit_data

    def _load_commit_data(self):
        self._commit_data = []
        for branch in self._repo.listall_branches():
            for commit in self._repo.walk(self._repo
                                          .lookup_branch(branch).target):
                self._commit_data.append((
                    commit.hex,
                    commit.author.email,
                    commit.author.name,
                    commit.author.time
                ))

    @staticmethod
    def _named2dict(named):
        return {field: named[i] for i, field in enumerate(named._fields)}

    def authors(self):
        return map(self._named2dict,
                   authors(map(lambda cd: cd[:3],
                               self.commit_data)))

    def histogram(self, author=None, by='quarter'):
        divisors = {'year': YEAR,
                    'month': MONTH,
                    'quarter': QUARTER}
        divisor = divisors.get(by)
        if divisor is None:
            raise ValueError("Wrong 'by' argument ({}), should be one of {}",
                             by, list(divisors.keys()))
        return {
            'fields': ['start', 'end', 'commits'],
            'data': core_histogram(self.commit_data, author, divisor)
        }
