from pytest import fixture

from workingless import countries


@fixture(scope='session')
def col_fixture():
    return countries.COL()


@fixture(scope='session')
def mex_fixture():
    return countries.MEX()
