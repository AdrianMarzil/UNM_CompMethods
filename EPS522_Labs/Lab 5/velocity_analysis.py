# velocity_analysis.py

import numpy as np
import pandas as pd
import glob

def import_tenv3(filename):
    data = pd.read_csv(filename, delimiter='\s+')
    return data

def fit_timeseries(tlist, ylist):
    coeffs = np.polyfit(tlist, ylist, 1)
    residuals = ylist - np.polyval(coeffs, tlist)
    sigma = np.sqrt(np.sum(residuals**2) / (len(tlist) - 2))
    sigma_coeffs = sigma / np.sqrt(np.sum((tlist - np.mean(tlist))**2))
    return coeffs[0], sigma_coeffs

def fit_velocities(filename, direction):
    data = import_tenv3(filename)
    tlist = data['yyyy.yyyy'].values
    ylist = data[direction].values
    velocity, uncertainty = fit_timeseries(tlist, ylist)
    return velocity, uncertainty

def get_coordinates(filename):
    data = import_tenv3(filename)
    latitude = np.mean(data['_latitude(deg)'].values)
    longitude = np.mean(data['_longitude(deg)'].values)
    elevation = np.mean(data['__height(m)'].values)
    return latitude, longitude, elevation

def fit_all_velocities(folder, pattern):
    filenames = glob.glob(f"{folder}/{pattern}")
    sites = []
    coordinates = []
    elevation = []
    velocities_up = []
    uncertainties_up = []
    velocities_north = []
    uncertainties_north = []
    velocities_east = []
    uncertainties_east = []
    for filename in filenames:
        site = filename.split('/')[-1].split('.')[0]
        lat, lon, elev = get_coordinates(filename)
        coordinates.append([lat, lon])
        elevation.append(elev)
        
        vel_up, unc_up = fit_velocities(filename, '____up(m)')
        velocities_up.append(vel_up)
        uncertainties_up.append(unc_up)

        vel_north, unc_north = fit_velocities(filename, '_north(m)')
        velocities_north.append(vel_north)
        uncertainties_north.append(unc_north)

        vel_east, unc_east = fit_velocities(filename, '__east(m)')
        velocities_east.append(vel_east)
        uncertainties_east.append(unc_east)

        sites.append(site)

    df = pd.DataFrame({
        'Site': sites,
        'Coordinates': coordinates,
        'Elevation': elevation,
        'Velocity_Up': velocities_up,
        'Uncertainty_Up': uncertainties_up,
        'Velocity_North': velocities_north,
        'Uncertainty_North': uncertainties_north,
        'Velocity_East': velocities_east,
        'Uncertainty_East': uncertainties_east
    })

    return df
