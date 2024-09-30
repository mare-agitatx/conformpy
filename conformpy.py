import matplotlib.pyplot as plt
import numpy as np
import sys
import configparser


def merge_lists_into_a_list_of_tuples(list1, list2):
    merged_list = list(zip(list1, list2))
    return merged_list


def parametrization(x_sequence, y_sequence, complex_formula):
    '''
    '''

    real_sequence, imag_sequence = [], []
    xy_points_list = merge_lists_into_a_list_of_tuples(x_sequence, y_sequence)
    f = lambda z: eval(complex_formula)
    
    for x_val, y_val in xy_points_list:
        z = complex(x_val, y_val)
        w = f(z)
        real_sequence.append(w.real)
        imag_sequence.append(w.imag)

    return (real_sequence, imag_sequence)


def grid_list_maker(start, stop, step):
    '''
    '''
    grid_list_values = np.arange(start, stop + step, step)
    return grid_list_values


def plot_a_2d_curve_given_the_parametrization(x_sequence, y_sequence,
                                              complex_function_formula,
                                              plot_color, plot_alpha):
    '''
    '''
    curve = parametrization(x_sequence, y_sequence,
                            complex_function_formula)
    real_values = curve[0]
    imag_values = curve[1]
    plt.plot(real_values, imag_values, color = plot_color, alpha = plot_alpha)


def making_the_transformed_real_curves(x_grid, y_grid,
                                       complex_function_formula,
                                       render_sample_size, alpha_value):
    '''The 2 following functions generate the parametrized lines starting from
    the same grid above and then transforms it following the parametrization
    rule that corresponds to the chosen complex function to be represented.
    First, the real grid lines, the x ones.'''

    t_start, t_stop = x_grid[0], x_grid[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)

    y_temp = np.ones(render_sample_size) * y_grid[0]
    plot_a_2d_curve_given_the_parametrization(t, y_temp,
                                              complex_function_formula,
                                              'red', alpha_value)
    for y_value in y_grid[1:-1]:
        y_temp = np.ones(render_sample_size) * y_value
        plot_a_2d_curve_given_the_parametrization(t, y_temp,
                                                  complex_function_formula,
                                                  'coral', alpha_value)
    y_temp = np.ones(render_sample_size) * y_grid[-1]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 
                                              complex_function_formula,
                                              'magenta', alpha_value)


def making_the_transformed_imaginary_curves(x_grid, y_grid,
                                            complex_function_formula,
                                            render_sample_size, alpha_value):
    '''And now for the y ones, the imaginary lines.'''

    t_start, t_stop = y_grid[0], y_grid[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)

    x_temp = np.ones(render_sample_size) * x_grid[0]
    plot_a_2d_curve_given_the_parametrization(x_temp, t,
                                              complex_function_formula,
                                              'blue', alpha_value)
    for x_value in x_grid[1:-1]:
        x_temp = np.ones(render_sample_size) * x_value
        plot_a_2d_curve_given_the_parametrization(x_temp, t,
                                                  complex_function_formula,
                                                  'skyblue', alpha_value)
    x_temp = np.ones(render_sample_size) * x_grid[-1]
    plot_a_2d_curve_given_the_parametrization(x_temp, t,
                                              complex_function_formula,
                                              'lime', alpha_value)


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
    '''
    '''
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title('The original grid, f(z) = z')
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    making_the_identity_grid(x_grid, y_grid, alpha_value)


def plot_the_transformed_curves(x_grid, y_grid, graph_title,
                                complex_function_formula,
                                render_sample_size, alpha_value,
                                are_the_real_curves_shown,
                                are_the_imaginary_curves_shown):
    '''
    '''
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title(graph_title)
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    if are_the_real_curves_shown is True:
        making_the_transformed_real_curves(x_grid, y_grid,
                                           complex_function_formula,
                                           render_sample_size, alpha_value)
    if are_the_imaginary_curves_shown is True:
        making_the_transformed_imaginary_curves(x_grid, y_grid,
                                                complex_function_formula,
                                                render_sample_size, 
                                                alpha_value)


###############################################################################
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input given. Exiting...')
        print('Please input the configuration filename on the command line.')
        sys.exit()

    # import the parameters from CLI specified input file
    config = configparser.ConfigParser()
    input_file = sys.argv[1]
    config.read(input_file)
    
    print('Collecting parameters...')
    x_grid_start = float(config.get('parameters', 'x_grid_start'))
    x_grid_stop = float(config.get('parameters', 'x_grid_stop'))
    x_grid_step = float(config.get('parameters', 'x_grid_step'))
    y_grid_start = float(config.get('parameters', 'y_grid_start'))
    y_grid_stop = float(config.get('parameters', 'y_grid_stop'))
    y_grid_step = float(config.get('parameters', 'y_grid_step'))
    render_sample_size = int(config.get('parameters', 'render_sample_size'))
    is_the_ident_grid_shown = config.getboolean('parameters',
                                                'is_the_ident_grid_shown')
    are_the_real_curves_shown = config.getboolean('parameters',
                                                  'are_the_real_curves_shown')
    are_the_imag_curves_shown = config.getboolean('parameters',
                                                  'are_the_imag_curves_shown')
    alpha_value = float(config.get('parameters', 'alpha_value'))
    graph_title = config.get('parameters', 'graph_title')
    complex_formula = config.get('function', 'f_z')
    
    # making the grids of values
    x_grid_list = grid_list_maker(x_grid_start,
                                  x_grid_stop, x_grid_step)
    y_grid_list = grid_list_maker(y_grid_start,
                                  y_grid_stop, y_grid_step)
    
    # preparing the plots
    plt.figure(1)
    plot_the_transformed_curves(x_grid_list, y_grid_list, graph_title,
                                complex_formula,
                                render_sample_size, alpha_value,
                                are_the_real_curves_shown,
                                are_the_imag_curves_shown)
    if is_the_ident_grid_shown is True:
        plt.figure(2)
        plot_the_identity_grid(x_grid_list, y_grid_list, alpha_value)
    plt.show()
