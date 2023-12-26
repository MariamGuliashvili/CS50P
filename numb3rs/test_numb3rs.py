import pytest
from numb3rs import validate

def test_validate_valid_ip():
    assert validate("192.168.0.1") == True

def test_validate_invalid_ip():
    assert validate("192.168.0") == False
    assert validate("192.168.0.256") == False
    assert validate("256.168.0.1") == False
    assert validate("192.168.0.-1") == False

def test_validate_edge_cases():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
