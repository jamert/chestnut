chestnut
========

Library for extracting information for Humane Registry from git repository.


Usage:
------

Given repository location you can get main contributors as::

  >>> import chestnut
  >>> repo = chestnut.repo('./r2d2.git')
  >>> print repo.authors()
  {'John Doe': 96,
   'Mary Dowell': 35}
