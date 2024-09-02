from conformpy import *
import pytest


def test_merge_lists_into_a_list_of_tuples():
    '''
    '''
    list1, list2 = [1, 2, 'a'], [4, 5, 'b']
    tuples_list = [(1, 4), (2, 5), ('a', 'b')]
    assert merge_lists_into_a_list_of_tuples(list1, list2) == tuples_list


def test_parametrization():
    '''
    '''
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
            assert expected[i][j] == pytest.approx(observed[i][j])


def test_grid_list_maker():
    '''
    '''
    observed = grid_list_maker(0., 2., .5)
    expected = np.array([0., 0.5, 1., 1.5, 2.])

    assert type(observed) == type(expected)
    assert len(observed) == len(expected)
    for i in range(len(observed)):
        assert observed[i] == pytest.approx(expected[i])


#def test_plot_a_2d_curve_given_the_parametrization()



#def test_making_the_transformed_real_curves()



#def test_making_the_transformed_imaginary_curves()



#def test_making_the_identity_grid()



#def test_plot_the_identity_grid()



#def test_plot_the_transformed_curves()


