import Lab2.bmi as bmi
def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73, 50)
    print(result)
    assert (result == -1)

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 65)
    print(result)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 80)
    print(result)
    assert (result == 1)