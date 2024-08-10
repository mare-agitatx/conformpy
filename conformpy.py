import matplotlib.pyplot as plt
import numpy as np
GRAPH_TITLE = 'f(z) = z^2 -z -1'
X_GRID_START = -10
X_GRID_STOP = 10
X_GRID_STEP = .5
Y_GRID_START = -10
Y_GRID_STOP = 10
Y_GRID_STEP = .5
LINSPACE_PARAMETER_SIZE = 200
IS_THE_IDENTITY_GRID_SHOWN = True
ARE_THE_REAL_CURVES_SHOWN = True
ARE_THE_IMAGINARY_CURVES_SHOWN = True
ALPHA_VALUE = 0.75


def complex_function_formula(z):
    return (z**2 -z -1)
    
    
def point_parametrization(x, y):
    z = complex(x, y)
    w = complex_function_formula(z)
    return w.real, w.imag

    
def grid_list_maker(start, stop, step):
    grid_list_values = np.arange(start, stop + step, step)
    return grid_list_values
    

def plot_a_2d_curve_given_the_parametrization(x_inputlist, y_inputlist,
plot_color, plot_alpha):
    x_axis, y_axis = [], []
    for x in x_inputlist:
        for y in y_inputlist:
            parametrized_point = point_parametrization(x, y)
            x_axis.append(parametrized_point[0])
            y_axis.append(parametrized_point[1])
    plt.plot(x_axis, y_axis, color = plot_color, alpha = plot_alpha)

    
# the 2 following functions generate the parametrized lines starting from  
# the same grid above and then transforms it following the parametrization 
# rule that corresponds to the chosen complex function to be represented.
# First, the real grid lines, the x ones
def making_the_transformed_real_curves(x_grid_list, y_grid_list, sample_size,
alpha_value):
    t_start, t_stop = y_grid_list[0], y_grid_list[-1]
    t = np.linspace(t_start, t_stop, sample_size)
    
    x_temp = np.ones(len(t)) * x_grid_list[0]
    plot_a_2d_curve_given_the_parametrization(x_temp, t,  'blue',
    alpha_value)
    for x_value in x_grid_list[1:-1]:
        x_temp = np.ones(len(t)) * x_value
        plot_a_2d_curve_given_the_parametrization(x_temp, t, 'skyblue',
        alpha_value)
    x_temp = np.ones(len(t)) * x_grid_list[-1]
    plot_a_2d_curve_given_the_parametrization(x_temp, t, 'lime',
    alpha_value)
    
    
# and now for the y ones, the imaginary lines    
def making_the_transformed_imaginary_curves(x_grid_list, y_grid_list,
sample_size, alpha_value):
    t_start, t_stop = x_grid_list[0], x_grid_list[-1]
    t = np.linspace(t_start, t_stop, sample_size)   
    
    y_temp = np.ones(len(t)) * y_grid_list[0]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'red',
    alpha_value)  
    for y_value in y_grid_list[1:-1]:
        y_temp = np.ones(len(t)) * y_value
        plot_a_2d_curve_given_the_parametrization(t, y_temp, 'coral',
        alpha_value)
    y_temp = np.ones(len(t)) * y_grid_list[-1]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'magenta',
    alpha_value)


def plot_the_transformed_curves(x_grid_list, y_grid_list, linspace_parameter_size, alpha_value):
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title(GRAPH_TITLE)
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    if ARE_THE_REAL_CURVES_SHOWN is True:
        making_the_transformed_real_curves(x_grid_list, y_grid_list,
        linspace_parameter_size, alpha_value)
    if ARE_THE_IMAGINARY_CURVES_SHOWN is True:
        making_the_transformed_imaginary_curves(x_grid_list, y_grid_list,
        linspace_parameter_size, alpha_value)


# plotting the cartesian grid that is fed as input for the transformed curves, 
# in order to have a reference for the conformal maps' transformation;
# last lines and first lines are outside the for cycle in order to let
# the user set different colors for them, as to identify them
def making_the_identity_grid(x_grid_list_values, y_grid_list_values, alpha_value):
    x_minimum, x_maximum = x_grid_list_values[0], x_grid_list_values[-1]
    y_minimum, y_maximum = y_grid_list_values[0], y_grid_list_values[-1]
    
    plt.vlines(x = x_minimum, ymin = y_minimum, ymax = y_maximum, 
    color = 'red', alpha = alpha_value)
    for value in x_grid_list_values[1:-1]:
        plt.vlines(x = value, ymin = y_minimum, ymax = y_maximum,
        color = 'coral', alpha = alpha_value)    
    plt.vlines(x = x_maximum, ymin = y_minimum, ymax = y_maximum,
    color = 'magenta', alpha = alpha_value)

    plt.hlines(y = y_minimum, xmin = x_minimum, xmax = x_maximum,
    color = 'blue', alpha = alpha_value)
    for value in y_grid_list_values[1:-1]:
        plt.hlines(y = value, xmin = x_minimum, xmax = x_maximum,
        color = 'skyblue', alpha = alpha_value)
    plt.hlines(y = y_maximum, xmin = x_minimum, xmax = x_maximum,
    color = 'lime', alpha = alpha_value)
        

def plot_the_identity_grid(x_grid_list, y_grid_list, alpha_value):
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title('The original grid, f(z) = z')
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    making_the_identity_grid(x_grid_list, y_grid_list, alpha_value)
    
    
###############################################################################
if __name__ == "__main__":
    x_grid_list = grid_list_maker(X_GRID_START, X_GRID_STOP, X_GRID_STEP)
    y_grid_list = grid_list_maker(Y_GRID_START, Y_GRID_STOP, Y_GRID_STEP)
    plt.figure(1)
    plot_the_transformed_curves(x_grid_list, y_grid_list,
    LINSPACE_PARAMETER_SIZE, ALPHA_VALUE)

    if IS_THE_IDENTITY_GRID_SHOWN is True:
        plt.figure(2)
        plot_the_identity_grid(x_grid_list, y_grid_list, ALPHA_VALUE)
    
    plt.show()
