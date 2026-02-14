from GUI import calculate_stress, cal_strain, calculate_thermal_expansion
from pytest import approx
import pytest

def test_calculate_stress():
    assert calculate_stress(12,8) == approx(1.5, abs=0.001)
    assert calculate_stress(50,16) == approx(3.125, abs=0.001)
    assert calculate_stress(100, 14.4) == approx(6.944, abs=0.001)
    assert calculate_stress(120, 17.3) == approx(6.936, abs=0.001)




def test_cal_strain():
    assert cal_strain(10, 12) == approx(0.200, abs=0.001)
    assert cal_strain(8, 9) == approx(0.125, abs=0.001)
    assert cal_strain(20, 16) == approx(-0.200, abs=0.001)
    assert cal_strain(82, 64) == approx(-0.220, abs=0.001)

def test_calculate_thermal_expansion():
    assert calculate_thermal_expansion(0.000023, 2,100) == approx(0.0046, abs=0.001)
    assert calculate_thermal_expansion(0.0000165, 4, 50) == approx(0.0033, abs=0.001)
    assert calculate_thermal_expansion(0.000011, 3, 25) == approx(0.000825, abs=0.001)
    assert calculate_thermal_expansion(0.000016, 0.9, 60) == approx(0.000864, abs=0.001)
    assert calculate_thermal_expansion(0.000019, 8, 75) == approx(0.0114, abs=0.001)



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])