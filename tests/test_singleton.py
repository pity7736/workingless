from workingless.countries import Mexico, Colombia


def test_singleton():
    colombia0 = Colombia()
    colombia1 = Colombia()
    mexico0 = Mexico()
    mexico1 = Mexico()

    assert colombia0 is colombia1
    assert mexico0 is mexico1
    assert colombia0 is not mexico0
    assert colombia1 is not mexico1
