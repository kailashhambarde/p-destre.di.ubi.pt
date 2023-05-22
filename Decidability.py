import numpy as np

def calculate_distance(mu_G, mu_I, sigma_G, sigma_I):
    """
    Function to calculate distance according to the provided formula.

    Args:
        mu_G: Mean of genuine scores.
        mu_I: Mean of impostor scores.
        sigma_G: Standard deviation of genuine scores.
        sigma_I: Standard deviation of impostor scores.

    Returns:
        distance: Calculated distance value.
    """
    try:
        distance = (mu_G - mu_I) / np.sqrt(sigma_G + sigma_I)
    except ZeroDivisionError:
        print("Standard deviation cannot be zero.")
        return None
    except Exception as e:
        print("Error occurred: ", str(e))
        return None

    return distance
