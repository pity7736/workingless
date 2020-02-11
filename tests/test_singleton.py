from workingless.countries import MEX, COL


def test_singleton():
    colombia0 = COL()
    colombia1 = COL()
    mexico0 = MEX()
    mexico1 = MEX()

    assert colombia0 is colombia1
    assert mexico0 is mexico1
    assert colombia0 is not mexico0
    assert colombia1 is not mexico1
