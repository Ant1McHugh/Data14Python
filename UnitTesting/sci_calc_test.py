from sci_calc import scicalc

my_sci_calc = scicalc()

def test_find_sqrt():
    assert my_sci_calc.find_sqrt(100) == 10.0


def test_find_ceil():
    assert my_sci_calc.find_ceil(12.7) == 13


