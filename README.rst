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
  >>> print repo.histogram(author='John Doe',
                           by='quarter')
  {'fields': ['start', 'end', 'commits'],
   'data': [
     (1420070400, 1427846400, 43),
     (1427846400, 1435708800, 34),
     (1435708800, 1443657600, 19)
   ]}
