# tidal_analysis.py

import numpy as np
import pandas as pd
import glob

def import_rlrdata(filename):
    data = pd.read_csv(filename, delimiter=';', header=None, usecols=[0, 1], names=['yyyy.yyyy', 'elevation'])
    data.replace(-9999, np.nan, inplace=True)  # Replace -9999 with NaN
    return data

def fit_timeseries(tlist, ylist):
    coeffs = np.polyfit(tlist, ylist, 1)
    residuals = ylist - np.polyval(coeffs, tlist)
    sigma = np.sqrt(np.sum(residuals**2) / (len(tlist) - 2))
    sigma_coeffs = sigma / np.sqrt(np.sum((tlist - np.mean(tlist))**2))
    return coeffs[0], sigma_coeffs

def fit_tide_gauge(filename):
    data = import_rlrdata(filename)
    tlist = data['yyyy.yyyy'].values
    ylist = data['elevation'].values + 3.096  # Adding 3.096 to all elevation values
    rate, uncertainty = fit_timeseries(tlist, ylist)
    return rate, uncertainty

def fit_all_rates(folder, pattern):
    filenames = glob.glob(f"{folder}/{pattern}")
    stations = []
    rates = []
    uncertainties = []
    for filename in filenames:
        station = filename.split('/')[-1].split('.')[0]
        rate, uncertainty = fit_tide_gauge(filename)
        stations.append(station)
        rates.append(rate)
        uncertainties.append(uncertainty)
    df = pd.DataFrame({
        'Station': stations,
        'Rate (m)': rates,
        'Uncertainty': uncertainties
    })
    return df
