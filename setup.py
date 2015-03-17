import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('chestnut/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='chestnut',
    version=version,
    url='http://github.com/jamert/chestnut/',
    license='BSD',
    author='Artem Dayneko',
    author_email='dayneko.ab@gmail.com',
    description='Library for extracting information for humane registry '
                'from git repo',
    long_description=__doc__,
    packages=['chestnut'],
    # platforms='any',
    install_requires=[
        'pygit2==0.22.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
