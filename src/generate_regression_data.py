import numpy as np 

def poly_val(x,coeff_arr, degree):
    sum = 0
    for i in range(0,degree+1):
        sum += coeff_arr[i] * (x ** i)
    return sum


def generate_regression_data(degree, N, amount_of_noise=1.0):
    """
    Generate two numpy arrays that have a roughly polynomial relationship 
    between them of degree 'degree'. The two arrays should have size
    'N'. The values in x should range between -1 and 1. The coefficients of the
    polynomial are chosen at random between -10 and 10.
    
    Generate `y`, the response variable by using the random coefficients and the 
    x data using a polynomial relation of degree `degree`.
    
    After this, you should add a bit of noise (dictated by `amount_of_noise`) in the
    following way.

    Reminder, you can add random noise to the output of a function by simply doing:
        f'(x) = f(x) + N(0, std)
    where N(0, std) is a draw from a normal distribution with mean 0 and standard deviation 1.

    In code, that looks like:
        y += np.random.normal(loc=0.0, scale=std, size=y.shape)

    As `amount_of_noise` increases, the data should become harder and harder to fit.
    
    The `amount_of_noise` is dictated by the distribution of y. After generating y (without noise),
    measure the standard deviation of y (with np.std(y)). Then add noise to y as a multiple of the
    standard deviation of `y`. For example if y has a standard deviation of 2.0, and 
    `amount_of_noise = 1.5`, then:
        
        y_noise = y + np.random.normal(loc=0.0, scale=1.5*2.0, size=y.shape)

    For Polyynomial regression, the N dimension array for x doesn't need multiple attributes because we are
    working with polynomial regression.

    Args:
        degree (int): degree of polynomial that relates the output x and y
        N (int): number of points to generate
        amount_of_noise (float): amount of random noise to add to the relationship 
            between x and y.
    Returns:
        x (np.ndarray): explanatory variable of size N, ranges between -1 and 1.
        y (np.ndarray): response variable of size N.
            responds to x as a polynomial of degree. 

    """
    x = np.random.uniform(-1,1,N)
    coeffs = np.random.uniform(-10,10,degree+1)
    y = np.empty(N)
    for i in range(0, N):
        y[i] = poly_val(x[i],coeffs,degree)
    y_std = np.std(y)
    noise_Scale = y_std * amount_of_noise
    y = y + np.random.normal(loc=0.0, scale = noise_Scale, size = y.shape)
    return x, y
    raise NotImplementedError()
