import pygit2
from .core import authors


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
                ))

    @staticmethod
    def _named2dict(named):
        return {field: named[i] for i, field in enumerate(named._fields)}

    def authors(self):
        return map(self._named2dict, authors(self.commit_data))

