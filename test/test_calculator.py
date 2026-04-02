from app.calculator import sum, resta

def test_sum():
    assert sum(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2