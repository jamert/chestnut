chestnut
========

Library for extracting information for Humane Registry from git repository.


Usage:
------

Given repository location you can get main contributors as::

  >>> import chestnut
  >>> repo = chestnut.Repository('./r2d2.git')
  >>> print repo.authors()
  [{'name': 'John Doe',
    'email': 'j.doe@mail.com',
    'commit_count': 96},
   {'name': 'Mary Dowell',
    'email': 'm.dowell@mail.com',
    'commit_count': 35}]
