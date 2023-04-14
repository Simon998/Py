import fibonacci_sequence

def test_fibonacci_sequence():
    # Test the first 5 numbers in the Fibonacci sequence
    assert fibonacci_sequence.get_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    
    # Test the first 10 numbers in the Fibonacci sequence
    assert fibonacci_sequence.get_fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    # Test the first 0 numbers in the Fibonacci sequence
    assert fibonacci_sequence.get_fibonacci_sequence(0) == []
