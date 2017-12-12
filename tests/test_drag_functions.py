import sys
sys.path.append('..')
from openaero.aerodynamics import drag_functions

def test_drag():
    assert drag_functions.drag(1.2922, 13, 0.5, 0.25) == 13.6488625
