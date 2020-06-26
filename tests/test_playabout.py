import sys

# add parent path 
sys.path.append("..")

from mech.playabout import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1    
    assert factorial(3) == 6