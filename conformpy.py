import matplotlib.pyplot as plt
import numpy as np
from inputvalues import *
    
    
def is_iterable(something):
    try:
        iter(something)
        return True
    except TypeError:
        return False


def make_me_iterable(something):
    if is_iterable(something) is True:
        return something
    else:
        list_out = []
        list_out.append(something)
        return list_out


def parametrization(x, y):
    x_seq, y_seq = make_me_iterable(x), make_me_iterable(y)
    real_out, imag_out = [], []
    
    for x in x_seq:
        for y in y_seq:
            z = complex(x, y)
            w = complex_function_formula(z)
            real_out.append(w.real)
            imag_out.append(w.imag)
            
    return [np.array(real_out), np.array(imag_out)]

    
def grid_list_maker(start, stop, step):
    grid_list_values = np.arange(start, stop + step, step)
    return grid_list_values
    

def plot_a_2d_curve_given_the_parametrization(x_seq, y_seq,
plot_color, plot_alpha):
    curve = parametrization(x_seq, y_seq)
    real_values = curve[0]
    imag_values = curve[1]
    plt.plot(real_values, imag_values, color = plot_color, alpha = plot_alpha)

    
# the 2 following functions generate the parametrized lines starting from  
# the same grid above and then transforms it following the parametrization 
# rule that corresponds to the chosen complex function to be represented.
# First, the real grid lines, the x ones
def making_the_transformed_real_curves(x_grid_list, y_grid_list,
render_sample_size, alpha_value):
    t_start, t_stop = x_grid_list[0], x_grid_list[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)   
    
    y_temp = np.ones(render_sample_size) * y_grid_list[0]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'red',
    alpha_value)  
    for y_value in y_grid_list[1:-1]:
        y_temp = np.ones(render_sample_size) * y_value
        plot_a_2d_curve_given_the_parametrization(t, y_temp, 'coral',
        alpha_value)
    y_temp = np.ones(render_sample_size) * y_grid_list[-1]
    plot_a_2d_curve_given_the_parametrization(t, y_temp, 'magenta',
    alpha_value)
    
    
# and now for the y ones, the imaginary lines 
def making_the_transformed_imaginary_curves(x_grid_list, y_grid_list, 
render_sample_size, alpha_value):
    t_start, t_stop = y_grid_list[0], y_grid_list[-1]
    t = np.linspace(t_start, t_stop, render_sample_size)
    
    x_temp = x_grid_list[0]
    plot_a_2d_curve_given_the_parametrization(x_temp, t, 'blue',
    alpha_value)
    for x_value in x_grid_list[1:-1]:
        x_temp = x_value
        plot_a_2d_curve_given_the_parametrization(x_temp, t, 'skyblue',
        alpha_value)
    x_temp = x_grid_list[-1]
    plot_a_2d_curve_given_the_parametrization(x_temp, t, 'lime',
    alpha_value)
# TROVATO IL BUG!!!!!!!!!!! sta qui, se utilizzo l'array temporaneo
# come faccio sopra per le y per qualche ragione il codice impazzisce
# e aggiunge curve che non ci sono...   

def plot_the_transformed_curves(x_grid_list, y_grid_list,
render_sample_size, alpha_value):
    ax = plt.axes()
    ax.set_facecolor("linen")
    plt.title(GRAPH_TITLE)
    plt.ylabel('Im(z)')
    plt.xlabel('Re(z)')
    if ARE_THE_REAL_CURVES_SHOWN is True:
        making_the_transformed_real_curves(x_grid_list, y_grid_list,
        render_sample_size, alpha_value)
    if ARE_THE_IMAGINARY_CURVES_SHOWN is True:
        making_the_transformed_imaginary_curves(x_grid_list, y_grid_list,
        render_sample_size, alpha_value)


# plotting the cartesian grid that is fed as input for the transformed curves, 
# in order to have a reference for the conformal maps' transformation;
# last lines and first lines are outside the for cycle in order to let
# the user set different colors for them, as to identify them
def making_the_identity_grid(x_grid_list_values,
y_grid_list_values, alpha_value):
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
    RENDER_SAMPLE_SIZE, ALPHA_VALUE)

    if IS_THE_IDENTITY_GRID_SHOWN is True:
        plt.figure(2)
        plot_the_identity_grid(x_grid_list, y_grid_list, ALPHA_VALUE)
    
    plt.show()
