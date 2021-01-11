import numpy as np
from numpy.core.numeric import loads
import pandas as pd
import matplotlib.pyplot as plt

cities = [
    'Anaheim',
    'Antioch',
    'Bakersfield',
    'Beaumont',
    'Berkeley',
    'Bridgeport',
    'Burbank',
    'Chula Vista',
    'Columbia',
    'Concord',
    'Corona',
    'Costa Mesa',
    'Downey',
    'Durham',
    'East Los Angeles',
    'Edison',
    'El Monte',
    'Escondido',
    'Fairfield',
    'Fontana',
    'Fremont',
    'Fresno',
    'Fullerton',
    'Garden Grove',
    'Glendale',
    'Hayward',
    'Huntington Beach',
    'Independence',
    'Inglewood',
    'Irvine',
    'Jackson',
    'Lafayette',
    'Lakewood',
    'Lancaster',
    'Lincoln',
    'Long Beach',
    'Los Angeles',
    'Modesto',
    'Moreno Valley',
    'Newark',
    'Norwalk',
    'Oakland',
    'Oceanside',
    'Ontario',
    'Orange',
    'Oxnard',
    'Palmdale',
    'Paradise',
    'Pasadena',
    'Pomona',
    'Rancho Cucamonga',
    'Rialto',
    'Richmond',
    'Riverside',
    'Roseville',
    'Sacramento',
    'Salinas',
    'San Bernardino',
    'San Diego',
    'San Francisco',
    'San Jose',
    'Santa Ana',
    'Santa Clara',
    'Santa Clarita',
    'Santa Rosa',
    'Simi Valley',
    'Spring Valley',
    'Stockton',
    'Sunnyvale',
    'Thornton',
    'Thousand Oaks',
    'Torrance',
    'Vallejo',
    'Visalia',
    'Washington',
    'West Covina',
    'Westminster',
    'Windsor',
]

land_temp_cities = pd.read_csv(
    #'.../GlobalLandTemperaturesByCity.csv',
)

# read and transform file
la_temps = land_temp_cities.loc[land_temp_cities['City'] == 'San Jose', ['dt','AverageTemperature']]
la_temps.columns = ['Date','Temp']
la_temps['Date'] = pd.to_datetime(la_temps['Date'])
la_temps.reset_index(drop=True, inplace=True)
la_temps.set_index('Date', inplace=True)

# print temp values from year of 2012
la_temps = la_temps.loc['2012-01-01':'2013-01-01']
print(la_temps)
