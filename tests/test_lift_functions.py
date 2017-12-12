import sys
sys.path.append('..')
from openaero.aerodynamics import lift_functions

def test_lift():
    assert lift_functions.lift(1.2922, 13, 0.5, 0.25) == 13.6488625
