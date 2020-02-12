import os

from setuptools import setup, find_packages


install_requires = [
    'python-dateutil==2.8.1'
]

test_require = [
    'pytest==5.3.5',
    'pytest-cov==2.8.1',
]


with open(os.path.join(os.path.dirname(__file__), 'workingless', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break

with open('README.rst') as f:
    readme = f.read()


setup(
    name='workingless',
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    author='Julián Cortés',
    author_email='pity7736@gmail.com',
    description='Holidays and working days calculations',
    long_description=readme,
    keywords='holiday working-day',
    url='https://github.com/pity7736/workingless',
    tests_require=test_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ]
)
