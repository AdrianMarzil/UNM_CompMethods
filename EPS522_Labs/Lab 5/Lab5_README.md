## Lab 5: Abstraction - Modules

### Module: velocity_analysis.py

<b>Python functions include:</b> 
1. <b>import_tenv3:</b> Imports data from .tenv3 files using the correct delimiter 'tab'
2. <b>fit_timeseries:</b> Calculates least squares velocity and uncertainty for displacement values
3. <b>fit_velocities:</b> Uses the 'fit_timeseries function to pull velocity and uncertainty calculations for each direction (Up, North, East).
4. <b>get_coordinates:</b> Pulls the latitude, longitude, and elevation data for each site (file), and calculates the mean latitude, longitude, and elevation.
5. <b>fit_all_velocities:</b> Utilizes 'glob' to look through all the .tenv3 files to get the velocity and uncertainty calculations for each direction (North, East, Up), the mean coordinates (latidue, longitude), and mean elevation for each site (file)

<b> How to Use: </b>
1. Import module:
<br>
```import velocity_analysis```

2. Specify the folder and pattern for timeseries files
<br>
```folder_path = '/Users/Adrian/Documents/VS CODE/CompMethods_EPS522/Labs/Lab 5/timeseries'```
<br>
```file_pattern = '*.NA.tenv3'```

3. Use the module to estimate velocities for all sites
<br>
```df = velocity_analysis.fit_all_velocities(folder_path, file_pattern)```

4. Print the results
<br>
```print(df)```

5. Save the results to a CSV file
<br>
```df.to_csv('site_velocities.csv', index=False)```

### Module: tidal_analysis.py

<b>Python functions include:</b> 
1. <b>import_rlrdata:</b> Imports data from .rlrdata files using the correct delimiter ';'
2. <b>fit_timeseries:</b> Calculates least squares tidal rates and uncertainty for tidal elevations
3. <b>fit_tidal_gauge:</b> Uses the 'fit_timeseries function to pull tidal rates and uncertainty calculations
4. <b>fit_all_rates:</b> Utilizes 'glob' to look through all the .rlrdata files to get the tidal rages and uncertainty calculations for each site (file)

<b> How to Use: </b>
1. Import module:
<br>
```import tidal_analysis```

2. Specify the folder and pattern for your timeseries files
<br>
```folder_path = '/Users/Adrian/Documents/VS CODE/CompMethods_EPS522/Labs/Lab 5/tidal_timeseries'```
<br>
```file_pattern = '*.rlrdata'```

3.  Use the module to estimate tidal rates for all sites
<br>
```df = tidal_analysis.fit_all_rates(folder_path, file_pattern)```

4. Print the results
<br>
```print(df)```

5. Save the results to a CSV file
<br>
```df.to_csv('site_tides.csv', index=False)```