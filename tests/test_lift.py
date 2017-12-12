from .context import openaero

def test_lift():
    assert openaero.aerodynamics.lift_functions.lift(1.2922, 13, 0.5, 0.25) == 13.6488625
