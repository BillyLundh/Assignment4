import pytest
from datetime import datetime
from toll_calculator_buggy import TollCalculator

def test_get_total_toll_fee():
    dates = [datetime(2022, 1, 1, 6, 0), 
             datetime(2022, 1, 1, 6, 15),
             datetime(2022, 1, 1, 6, 45),
             datetime(2022, 1, 1, 7, 30)]
    expected_output = 50
    
    result = TollCalculator.get_total_toll_fee(dates)
    assert result == expected_output
    
def test_get_toll_fee_per_passing():
    date = datetime(2022, 7, 20, 6, 0)
    expected_output = 8
    
    result = TollCalculator.get_toll_fee_per_passing(date)
    
    assert result == expected_output
    
def test_is_toll_free_date():

    date = datetime(2022, 7, 1, 6, 0)
    expected_output = True
    
    result = TollCalculator.is_toll_free_date(date)

    assert result == expected_output
