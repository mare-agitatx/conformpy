import numpy as np
# input values for the algorithm
GRAPH_TITLE = 'f(z) = z**3 +z**2'
X_GRID_START = -10
X_GRID_STOP = 10
X_GRID_STEP = .2
Y_GRID_START = -10
Y_GRID_STOP = 10
Y_GRID_STEP = .2
RENDER_SAMPLE_SIZE = 200
IS_THE_IDENTITY_GRID_SHOWN = False
ARE_THE_REAL_CURVES_SHOWN = True
ARE_THE_IMAGINARY_CURVES_SHOWN = True
ALPHA_VALUE = 0.75


def complex_function_formula(z):
    return (z**3 +z**2)
