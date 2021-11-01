from series import __version__ 
from series.series import fibonacci , lucas , sum_series



def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_3():
    excepted = 2 
    actual = fibonacci(3)
    assert excepted == actual    

def test_fibonacci_7():
    excepted= 13 
    actual = fibonacci(7) 
    assert excepted == actual

def test_fibonacci_8():
    excepted = 21 
    actual = fibonacci(8)
    assert excepted == actual


def test_lucas_3() :
    excepted = 3 
    actual = lucas(2)
    assert excepted == actual    

def test_lucas_6() :
    excepted = 47 
    actual = lucas(8)
    assert excepted == actual


def test_sum_series():
   excepted = 8 
   actual = sum_series(6)
   assert excepted == actual

def test_sum_series_8():
   excepted = 47 
   actual = sum_series(8,2)
   assert excepted == actual

def test_sum_series_4():
   excepted = 21
   actual = sum_series(4,3,6)
   assert excepted == actual 

def test_sum_series_4():
   excepted = 27
   actual = sum_series(4,3,7)
   assert excepted == actual        