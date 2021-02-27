import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
from math import sqrt

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

def plot_variation(df):
    plt.figure(figsize=(22, 6))
    sns.lineplot(x=df.index, y=df['Temp'])
    plt.title('Temperature Variation in San Jose from 1900 until 2012')
    plt.show()


def plot_monthly_var(df, mean):
    pivot = pd.pivot_table(df, values='Temp', index='month', columns='year', aggfunc='mean')
    if mean:
        monthly_seasonality = pivot.mean(axis=1)
        monthly_seasonality.plot(figsize=(20, 6))
        plt.title('Monthly Temperatures in San Jose')
        plt.xlabel('Months')
        plt.ylabel('Temperature')
        plt.xticks([x for x in range(1, 13)])
    else:
        pivot.plot(figsize=(20, 6))
        plt.title('Yearly San Jose temperatures')
        plt.xlabel('Months')
        plt.ylabel('Temperatures')
        plt.xticks([x for x in range(1, 13)])
    plt.legend().remove()
    plt.show()

def check_moving_avg(df):
    year_avg = pd.pivot_table(df, values='Temp', index='year', aggfunc='mean')
    year_avg['10 Years MA'] = year_avg['Temp'].rolling(10).mean()
    first_ma = year_avg['10 Years MA'].iloc[9]
    last_ma = year_avg['10 Years MA'].iloc[-1]
    print(f'The average temperature in San Jose was {round(first_ma, 4)} in 1909')
    print(f'The average temperature in San Jose was {round(last_ma, 4)} in 2011')
    year_avg[['Temp', '10 Years MA']].plot(figsize=(20, 6))
    plt.title('Yearly AVG Temperatures in San Jose')
    plt.xlabel('Months')
    plt.ylabel('Temperature')
    plt.xticks([x for x in range(1900, 2012, 3)])
    plt.show()


land_temp_cities = pd.read_csv(
    '/Users/AaronLopes/datasets/GlobalLandTemperaturesByCity.csv',
)

# read, transform, and clean file
la_temps = land_temp_cities.loc[land_temp_cities['City'] == 'San Jose', ['dt', 'AverageTemperature']]
la_temps.columns = ['Date', 'Temp']
la_temps['Date'] = pd.to_datetime(la_temps['Date'])
bad_temp = la_temps['Temp'] < 0
la_temps[bad_temp] = 0.0
# la_temps['Temp'] = (1.8 * la_temps['Temp']) + 32
la_temps.reset_index(drop=True, inplace=True)
la_temps.set_index('Date', inplace=True)

# print temp values from year of 2012
la_temps = la_temps.loc['1900':'2013-01-01']
la_temps = la_temps.asfreq('M', method='bfill')

la_temps['month'] = la_temps.index.month
la_temps['year'] = la_temps.index.year
check_moving_avg(la_temps)

