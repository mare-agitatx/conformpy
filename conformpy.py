import matplotlib.pyplot as plt
import numpy as np
import inputvalues as IV
from pytest import approx


def merge_lists_into_a_list_of_tuples(list1, list2):
    merged_list = list(zip(list1, list2))
    return merged_list


def parametrization(x_sequence, y_sequence, complex_formula):
    '''
    '''

    real_sequence, imag_sequence = [], []
    list_of_tuples = merge_lists_into_a_list_of_tuples(x_sequence, y_sequence)

    for x_val, y_val in list_of_tuples:
        z = complex(x_val, y_val)
        w = complex_formula(z)
        real_sequence.append(w.real)
        imag_sequence.append(w.imag)

    return (real_sequence, imag_sequence)


def grid_list_maker(start, stop, step):
    grid_list_values = np.arange(start, stop + step, step)
    return grid_list_values


def plot_a_2d_curve_given_the_parametrization(x_sequence, y_sequence,
plot_color, plot_alpha):
    '''
    '''
    
    curve = parametrization(x_sequence, y_sequence,
    IV.complex_function_formula)
    real_values = curve[0]
    imag_values = curve[1]
    plt.plot(real_values, imag_values, color = plot_color, alpha = plot_alpha)


def making_the_transformed_real_curves(x_grid, y_grid,
render_sample_size, alpha_value):
    '''The 2 following functions generate the parametrized lines starting from
    the same grid above and then transforms it following the parametrization
    rule that corresponds to the chosen complex function to be represented.
    First, the real grid lines, the x ones.'''

    t_start, t_stop = x_grid[0], x_grid[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)

    y_temp = np.ones(render_sample_size) * y_grid[0]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'red',
    alpha_value)
    for y_value in y_grid[1:-1]:
        y_temp = np.ones(render_sample_size) * y_value
        plot_a_2d_curve_given_the_parametrization(t, y_temp, 'coral',
        alpha_value)
    y_temp = np.ones(render_sample_size) * y_grid[-1]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'magenta',
    alpha_value)


def making_the_transformed_imaginary_curves(x_grid, y_grid,
render_sample_size, alpha_value):
    '''And now for the y ones, the imaginary lines.'''

    t_start, t_stop = y_grid[0], y_grid[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)

    x_temp = np.ones(render_sample_size) * x_grid[0]
    plot_a_2d_curve_given_the_parametrization(x_temp, t, 'blue',
    alpha_value)
    for x_value in x_grid[1:-1]:
        x_temp = np.ones(render_sample_size) * x_value
        plot_a_2d_curve_given_the_parametrization(x_temp, t, 'skyblue',
        alpha_value)
    x_temp = np.ones(render_sample_size) * x_grid[-1]
    plot_a_2d_curve_given_the_parametrization(x_temp, t, 'lime',
    alpha_value)


# plotting the cartesian grid that is fed as input for the transformed curves,
# in order to have a reference for the conformal maps' transformation;
# last lines and first lines are outside the for cycle in order to let
# the user set different colors for them, as to identify them
def making_the_identity_grid(x_grid, y_grid, alpha_value):
    '''
    '''
    
    x_minimum, x_maximum = x_grid[0], x_grid[-1]
    y_minimum, y_maximum = y_grid[0], y_grid[-1]

    plt.vlines(x = x_minimum, ymin = y_minimum, ymax = y_maximum,
    color = 'red', alpha = alpha_value)
    for value in x_grid[1:-1]:
        plt.vlines(x = value, ymin = y_minimum, ymax = y_maximum,
        color = 'coral', alpha = alpha_value)
    plt.vlines(x = x_maximum, ymin = y_minimum, ymax = y_maximum,
    color = 'magenta', alpha = alpha_value)

    plt.hlines(y = y_minimum, xmin = x_minimum, xmax = x_maximum,
    color = 'blue', alpha = alpha_value)
    for value in y_grid[1:-1]:
        plt.hlines(y = value, xmin = x_minimum, xmax = x_maximum,
        color = 'skyblue', alpha = alpha_value)
    plt.hlines(y = y_maximum, xmin = x_minimum, xmax = x_maximum,
    color = 'lime', alpha = alpha_value)


def plot_the_identity_grid(x_grid, y_grid, alpha_value):
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title('The original grid, f(z) = z')
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    making_the_identity_grid(x_grid, y_grid, alpha_value)


def plot_the_transformed_curves(x_grid, y_grid,
render_sample_size, alpha_value):
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title(IV.GRAPH_TITLE)
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    if IV.ARE_THE_REAL_CURVES_SHOWN is True:
        making_the_transformed_real_curves(x_grid, y_grid,
        render_sample_size, alpha_value)
    if IV.ARE_THE_IMAGINARY_CURVES_SHOWN is True:
        making_the_transformed_imaginary_curves(x_grid, y_grid,
        render_sample_size, alpha_value)


###############################################################################
if __name__ == "__main__":
    x_grid_list = grid_list_maker(IV.X_GRID_START,
    IV.X_GRID_STOP, IV.X_GRID_STEP)
    y_grid_list = grid_list_maker(IV.Y_GRID_START,
    IV.Y_GRID_STOP, IV.Y_GRID_STEP)
    plt.figure(1)
    plot_the_transformed_curves(x_grid_list, y_grid_list,
    IV.RENDER_SAMPLE_SIZE, IV.ALPHA_VALUE)

    if IV.IS_THE_IDENTITY_GRID_SHOWN is True:
        plt.figure(2)
        plot_the_identity_grid(x_grid_list, y_grid_list, IV.ALPHA_VALUE)

    plt.show()
    
###############################################################################
def test_merge_lists_into_a_list_of_tuples():
    list1, list2 = [1, 2, 'a'], [4, 5, 'b']
    tuples_list = [(1, 4), (2, 5), ('a', 'b')]
    assert merge_lists_into_a_list_of_tuples(list1, list2) == tuples_list


def test_parametrization():
    x_list, y_list = [.1, 10.9], [.2, 20.8]
    xy_points = merge_lists_into_a_list_of_tuples(x_list, y_list)
    z = [complex(.1, .2), complex(10.9, 20.8)]
    reals, imags = [], []

    for point in xy_points:
        x, y = point[0], point[1]
        reals.append(x**2 - y**2)
        imags.append(2*x*y)
 
    def complex_formula(z):
        return z**2

    expected = [reals, imags]
    observed = parametrization(x_list, y_list, complex_formula)
    
    for i in range(2):
        for j in range(2):
            assert expected[i][j] == approx(observed[i][j])


def test_grid_list_maker():
    observed = grid_list_maker(0., 2., .5)
    expected = np.array([0., 0.5, 1., 1.5, 2.])

    assert type(observed) == type(expected)
    assert len(observed) == len(expected)
    for i in range(len(observed)):
        assert observed[i] == approx(expected[i])


#def test_plot_a_2d_curve_given_the_parametrization()
    


#def test_making_the_transformed_real_curves()
    


#def test_making_the_transformed_imaginary_curves()
    


#def test_making_the_identity_grid()
    


#def test_plot_the_identity_grid()
    


#def test_plot_the_transformed_curves()
    


