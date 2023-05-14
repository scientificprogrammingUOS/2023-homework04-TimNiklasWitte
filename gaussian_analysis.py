import numpy as np


def gaussian_analysis(loc, scale, lower_bound, upper_bound):
        
    if not type(loc) == type(scale) == type(lower_bound) == type(upper_bound) == int:
        raise ValueError("loc, scale, lower_bound and upper_bound must be integers")

    if lower_bound > upper_bound:
        raise ValueError("lower_bound must be smaller or equal than upper_bound")


    random_values = np.random.normal(loc=loc, scale=scale, size=(100))

    # Filtering 
    random_values = [value for value in random_values if lower_bound <= value and value <= upper_bound]

    mean = np.mean(random_values)
    std = np.std(random_values)

    return mean, std

if __name__ == "__main__":


    gaussian_analysis(0, 1, -1, 1)
