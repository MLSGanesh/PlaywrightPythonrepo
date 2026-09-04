'''
pre-requisite: install 'pytest-xdist' plug-in

pip install pytest-xdist

'''

import pytest

def test_one():
    print("running test one")
    assert True

def test_two():
    print("running test two")
    assert True

def test_three():
    print("running test three")
    assert True

def test_four():
    print("running test four")
    assert True

# pytest day17/test_parallel.py -s -v -n=2
# pytest day17/test_parallel.py -s -v -n 2
# n indicates number of workers required for the job. Because single worker will execute the task in serial pattern. If multiple workers are assigned task will be done by distributing among those
# Use 5 workers max: Going with more than 5 workers will delay the execution/performance as memory consumption occurs
