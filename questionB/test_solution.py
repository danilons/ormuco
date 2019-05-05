
from .solution import is_greater

def test_is_greater():
	assert is_greater("1.2", "1.1")

def test_different_patterns():
	assert is_greater("1.2", "1.19999999")

	assert is_greater("A", "123")  # ASCII 

	assert not is_greater("4.11", "4.2")

	assert is_greater("10", "3")

	assert not is_greater("3", "100")