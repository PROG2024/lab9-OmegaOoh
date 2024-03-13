"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import pytest
from counter import Counter


def test_counter_singleton():
    """ Test if the counter is singleton. """
    counter = Counter()
    counter2 = Counter()
    assert counter == counter2


def test_counter_count():
    """ Test if all counter have the same count"""
    counter = Counter()
    counter2 = Counter()
    assert counter.increment() == counter2.count

