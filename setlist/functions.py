import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
from scipy.stats import beta

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
    amplitude = (max_value - min_value) / 2
    intercept = max_value - amplitude
    x = np.arange(num_points)
    y = amplitude * np.cos(2 * np.pi * f * x / Fs) + intercept
    if show_plot:
        plt.plot(x, y, '-o')
        plt.show()
    return y


def scale(np_array, min_range = 0, max_range = 1):
    '''
    Scales a np array to 0 to 1 range

    Args:
        np_array (np_array): A numpy array of values
    Returns:
        a numpy array of the values scaled to a 0 to 1 range

    '''
    min_value = min(np_array)
    max_value = max(np_array)
    scaled_values = (max_range - min_range) * (np_array - min_value) / (max_value - min_value) + min_range
    return scaled_values


def discrete_normal(num_points, var_factor = 2, min_value=0, max_value=1, show_plot=False):
    '''
    Creates a discretized normal distribution

    Args:
        num_points (int): The number of points for the function to be discretized to.
        var_factor (float): The scalar multiplied by the number of points (i.e. var = num_points * var_factor)
        min_value (int, float): The lower bound of the function, defaulted to 0
        max_value (int, float): The upper bound of the function, defaulted to 1
        show_plot (bool): Bool to show the plot of the function, default to false

    Returns:
        A numpy array of the y values of the discretized normal distribution
    '''
    mu = num_points / 2
    variance = num_points * var_factor
    sigma = math.sqrt(variance)
    x = np.arange(num_points)
    y = scale(mlab.normpdf(x, mu, sigma), min_value, max_value)
    if show_plot:
        plt.plot(x,y, '-o')
        plt.show()
    return y

# discrete_bimodal(75, show_plot=True)

# discrete_normal(100, 2, show_plot=True)

def discrete_beta(num_points, a, b, min_value=0, max_value=1, show_plot=False):
    '''
    Creates a discretized beta distribution

    Args:
        num_points (int): The number of points for the function to be discretized to.
        a (float): alpha parameter of the beta distribution
        b (float): beta parameter of the beta distribution
        min_value (int, float): The lower bound of the function, defaulted to 0
        max_value (int, float): The upper bound of the function, defaulted to 1
        show_plot (bool): Bool to show the plot of the function, default to false

    Returns:
        A numpy array of the y values of the discretized normal distribution
    '''
    x = np.arange (0, num_points)
    y = scale(beta.pdf(x,a,b, scale = num_points), min_value, max_value)
    if show_plot:
        plt.plot(x,y,'-o')
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

