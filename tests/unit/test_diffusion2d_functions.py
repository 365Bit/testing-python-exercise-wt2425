"""
Tests for functions in class SolveDiffusion2D
"""

import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    nx, ny = 4., 6.
    solver = SolveDiffusion2D()
    solver.initialize_domain(2., 3., 0.5, 0.5)
    assert solver.nx == nx, "Returned nx does not match expected nx"
    assert solver.ny == ny, "Returned ny does not match expected ny"


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    dt = 0.0083
    solver = SolveDiffusion2D()
    solver.dx, solver.dy = 0.5, 0.25
    solver.initialize_physical_parameters(3., 365., 500.)
    assert pytest.approx(dt, abs=0.0001) == solver.dt, "Returned dt does not match expected dt"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.dx = solver.dy = 0.2
    solver.nx = solver.ny = 75
    solver.T_cold = 365.
    solver.T_hot = 500.

    solver_u = solver.set_initial_condition()

    r, cx, cy = 2, 5, 5
    r2 = r ** 2

    u = solver.T_cold * np.ones((solver.nx, solver.ny))

    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                u[i, j] = solver.T_hot

    assert pytest.approx(u, abs=0.01) == solver_u, "Returned initial condition does not match expected initial condition"