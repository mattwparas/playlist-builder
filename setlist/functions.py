import numpy as np
import matplotlib.pyplot as plt


def discrete_sin(num_points, periods, min_value=0, max_value = 1, show_plot=False):
    '''
    Discretizes a sin function to the number of points specified

    Args:
        num_points (int): The number of points for the function to be discretized to.
        periods (int): The number of periods of the sin function.
        min_value (int, float): The lower bound of the sin function, defaulted to 0
        max_value (int, float): The upper bound of the sin function, defaulted to 1
        show_plot (bool): Bool to show the plot of the function, default to false

    Returns:
        A numpy array of the y values of the discretized sin function
    '''
    Fs = num_points
    f = periods
    sample = num_points
    amplitude = (max_value - min_value) / 2
    intercept = max_value - amplitude
    x = np.arange(num_points)
    y = amplitude * np.sin(2 * np.pi * f * x / Fs) + intercept
    if show_plot:
        plt.plot(x, y, '-o')
        plt.show()
    return y

def discrete_cos(num_points, periods, min_value=0, max_value = 1, show_plot=False):
    '''
    Discretizes a sin function to the number of points specified

    Args:
        num_points (int): The number of points for the function to be discretized to.
        periods (int): The number of periods of the cos function.
        min_value (int, float): The lower bound of the cos function, defaulted to 0
        max_value (int, float): The upper bound of the cos function, defaulted to 1
        show_plot (bool): Bool to show the plot of the function, default to false

    Returns:
        A numpy array of the y values of the discretized cos function
    '''
    Fs = num_points
    f = periods
    sample = num_points
    amplitude = (1 - min_value) / 2
    intercept = 1 - amplitude
    x = np.arange(num_points)
    y = amplitude * np.cos(2 * np.pi * f * x / Fs) + intercept
    if show_plot:
        plt.plot(x, y, '-o')
        plt.show()
    return y

def discrete_linear(num_points, min_value=0, max_value=1):
    '''
    Discretizes a linear function to the number of points specified

    Args:
        num_points (int): The number of points for the function to be discretized to.
        min_value (int, float): The lower bound of the function, defaulted to 0
        max_value (int, float): The upper bound of the function, defaulted to 1

    Returns:
        A numpy array of the y values of the discretized linear function
    '''
    return np.linspace(min_value, max_value, num = num_points)

def discrete_random(num_points, min_value=0, max_value=1):
    '''
    Discretizes uniform function to the number of points specified

    Args:
        num_points (int): The number of points for the function to be discretized to.
        min_value (int, float): The lower bound of the function, defaulted to 0
        max_value (int, float): The upper bound of the function, defaulted to 1

    Returns:
        A numpy array of the y values of the samples from the uniform distribution
    '''
    return np.random.uniform(low = min_value, high = max_value, size = num_points)

