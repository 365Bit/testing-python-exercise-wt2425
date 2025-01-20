"""
Tests for functionality checks in class SolveDiffusion2D
"""

import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    dt = 0.0208
    solver.initialize_domain(2., 3., 0.5, 0.5)
    solver.initialize_physical_parameters(3., 365., 500.)

    assert pytest.approx(dt, abs=0.0001) == solver.dt, "Returned dt does not match expected dt"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    u = np.array([
        [300.0, 300.0, 300.0, 300.0, 300.0],
        [300.0, 300.0, 300.0, 300.0, 300.0],
        [300.0, 300.0, 300.0, 300.0, 300.0],
        [300.0, 300.0, 300.0, 300.0, 300.0],
        [300.0, 300.0, 300.0, 300.0, 300.0]
    ])

    solver.initialize_domain(0.5, 0.5, 0.1, 0.1)
    solver.initialize_physical_parameters(5., 300., 700.)
    solver_u = solver.set_initial_condition()

    assert pytest.approx(u, abs=0.01) == solver_u, "Returned initial condition does not match expected initial condition"