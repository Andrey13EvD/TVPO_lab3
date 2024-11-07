import main

def test_result():
    bank = main.BankInterest(100000, 2, 10)
    assert len(bank.ann_int()) == 2
    assert bank.ann_int() == (4614.49, 110747.82)

def test_diff_int():
    bank = main.BankInterest(100000, 2, 10)
    arr, total = bank.diff_int()
    assert len(arr) == 24
    assert round(total, 2) == 110747.82

if __name__ == '__main__':
    test_result()
    test_diff_int()
