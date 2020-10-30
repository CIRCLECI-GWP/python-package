from convrsn.distance import k2m, m2k

def test_k2m():
    assert round(k2m(1), 2) == 0.62

def test_m2k():
    assert round(m2k(1), 2) == 1.61
