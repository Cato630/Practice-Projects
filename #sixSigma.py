#sixSigma
import numpy as np 
import pandas as pd

def six_sigma(data, spec_limits):
    """
    Calculate Six Sigma metrics for a given data population.
    
    Parameters:
    - data: List or array of numerical values representing the data population.
    - spec_limits: Tuple of (lower_spec_limit, upper_spec_limit).
    
    Returns:
    - mean: The mean of the data.
    - std_dev: The standard deviation of the data.
    - dpm: Defects per million opportunities.
    - sigma_level: The sigma level of the process.
    """
    data = np.array(data)
    
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    lower_spec_limit, upper,_spec_limit = spec_limits
    defects = np.sum(data <lower_spec_limit) + np.sum(data > upper_spec_limit)
    opportunites = len(data)
    dpm=(defects / opportunites) * 1e6
    z_lower = (mean - lower_spec_limit) / std_dev
    z_upper = (upper_spec_limit - mean) / std_dev
    sigma_level = min(z_lower, z_upper)
    return mean, std_dev, dpm, sigma_level

def read_from_csv(file_path, column_name):
    df = pd.read_csv(file_path)
    return df[column_name].dropna().tolist()

def read_data_from_excel(file_path, sheet_name, column_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df[column_name].dropna().tolist()

file_path = 'data.csv'
column_name = 'data'
data_population = read_from_csv(file_path, column_name)
spec_limits = (0, 100)
mean, std_dev, dpm, sigma_level = six_sigma(data_population, spec_limits)
 
