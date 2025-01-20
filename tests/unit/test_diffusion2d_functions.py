"""
Tests for functions in class SolveDiffusion2D
"""

import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        nx, ny = 4., 6.
        self.solver.initialize_domain(2., 3., 0.5, 0.5)
        assert self.solver.nx == nx, "Returned nx does not match expected nx"
        assert self.solver.ny == ny, "Returned ny does not match expected ny"


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        dt = 0.0083
        self.solver.dx, self.solver.dy = 0.5, 0.25
        self.solver.initialize_physical_parameters(3., 365., 500.)
        self.assertAlmostEqual(self.solver.dt, dt, places=4, msg="Returned dt does not match expected dt")


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.dx = self.solver.dy = 0.2
        self.solver.nx = self.solver.ny = 75
        self.solver.T_cold = 365.
        self.solver.T_hot = 500.

        solver_u = self.solver.set_initial_condition()

        r, cx, cy = 2, 5, 5
        r2 = r ** 2

        u = self.solver.T_cold * np.ones((self.solver.nx, self.solver.ny))

        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r2:
                    u[i, j] = self.solver.T_hot

        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                self.assertAlmostEqual(u[i,j], solver_u[i,j], places=2, msg="Returned initial condition does not match expected initial condition")
