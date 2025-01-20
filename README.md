# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```bash
====================================================================================================================================== test session starts =======================================================================================================================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\Rene\source\repos\SSE\testing-python-exercise-wt2425
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                                                                                                                                                                                                    [ 40%]
tests\unit\test_diffusion2d_functions.py FFF                                                                                                                                                                                                                                                [100%]

============================================================================================================================================ FAILURES ============================================================================================================================================
_____________________________________________________________________________________________________________________________________ test_initialize_domain _____________________________________________________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        nx, ny = 4., 6.
        solver = SolveDiffusion2D()
        solver.initialize_domain(2., 3., 0.5, 0.5)
>       assert solver.nx == nx, "Returned nx does not match expected nx"
E       AssertionError: Returned nx does not match expected nx
E       assert 6 == 4.0
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x00000257BCF492B0>.nx

tests\unit\test_diffusion2d_functions.py:17: AssertionError
______________________________________________________________________________________________________________________________ test_initialize_physical_parameters _______________________________________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        dt = 0.0083
        solver = SolveDiffusion2D()
        solver.dx, solver.dy = 0.5, 0.25
        solver.initialize_physical_parameters(3., 365., 500.)
>       assert pytest.approx(dt, abs=0.0001) == solver.dt, "Returned dt does not match expected dt"
E       AssertionError: Returned dt does not match expected dt
E       assert 0.0083 ± 1.0e-04 == 0.21666666666666667
E
E         comparison failed
E         Obtained: 0.21666666666666667
E         Expected: 0.0083 ± 1.0e-04

tests\unit\test_diffusion2d_functions.py:29: AssertionError
-------------------------------------------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------------------------------------------
dt = 0.21666666666666667
___________________________________________________________________________________________________________________________________ test_set_initial_condition ___________________________________________________________________________________________________________________________________

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

>       assert pytest.approx(u, abs=0.01) == solver_u, "Returned initial condition does not match expected initial condition"
E       AssertionError: Returned initial condition does not match expected initial condition
E       assert approx([[365....0 ± 1.0e-02]]) == array([[365.,... 365., 365.]])
E
E         comparison failed. Mismatched elements: 309 / 5625:
E         Max absolute difference: 135.0
E         Max relative difference: 0.3698630136986301
E         Index    | Obtained | Expected
E       assert approx([[365....0 ± 1.0e-02]]) == array([[365.,... 365., 365.]])
E
E         comparison failed. Mismatched elements: 309 / 5625:
E         Max absolute difference: 135.0
E       assert approx([[365....0 ± 1.0e-02]]) == array([[365.,... 365., 365.]])
E
E       assert approx([[365....0 ± 1.0e-02]]) == array([[365.,... 365., 365.]])
E       assert approx([[365....0 ± 1.0e-02]]) == array([[365.,... 365., 365.]])
E
E         comparison failed. Mismatched elements: 309 / 5625:
E         Max absolute difference: 135.0
E         Max relative difference: 0.3698630136986301
E         Index    | Obtained | Expected
E         (16, 21) | 365.0    | 500.0 ± 1.0e-02
E         (16, 22) | 365.0    | 500.0 ± 1.0e-02...
E
E         ...Full output truncated (307 lines hidden), use '-vv' to show

tests\unit\test_diffusion2d_functions.py:55: AssertionError
==================================================================================================================================== short test summary info =====================================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: Returned nx does not match expected nx
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - AssertionError: Returned dt does not match expected dt
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError: Returned initial condition does not match expected initial condition
================================================================================================================================== 3 failed, 2 passed in 0.63s ===================================================================================================================================

```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
