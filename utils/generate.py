"""
Functions for generating nearest neighbors data
"""
import numpy as np

from scipy.stats import gaussian_kde

def uniform_random(vector_length, number_of_samples):
    """
    Just uses np.random to make a bunch of random examples 
    """
    return np.random.rand(vector_length, number_of_samples)

def density_function(axis):
    """
    Single density function, specifically lognorm density function.

    Just an example, many other density functionals will be appropriate
    so long as they maintain the same function signature
    """
    return gaussian_kde(axis).evaluate

def generate_density_functions(array, density_callback=density_function):
    """
    Given an array of samples, return a list of density functions across each axis
    """
    return [density_callback(axis) for axis in array]

def generate_sorted_lists(array):
    """
    Generates a list of sorted attributes

    First column is indices, second column is value
    """

def linear_search(query_vector, array):
    """
    Example of classic linear search to benchmark against
    """
    best = (0, 0)
    for i, entry in enumerate(array.T):
        distance = 1.0/(np.linalg.norm(query_vector - entry))
        if distance > best[0]:
            best = (distance, i)
    return best

def slater_search(query_vector, array, functions, sorted_lists):
    """
    Constant time nearest neighbors search?
    """
if __name__ == "__main__":
    a = uniform_random(2, 250000)
    test = np.array([0.5, 0.5])
    print linear_search(test, a)
