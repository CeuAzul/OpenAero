from .context import openaero

def test_drag():
    assert openaero.aerodynamics.drag_functions.drag(1.2922, 13, 0.5, 0.25) == 13.6488625
