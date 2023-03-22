import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    reg = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880, 2050)])
    y_pred = reg.slope * x_pred + reg.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    x2 = new_df['Year']
    y2 = new_df['CSIRO Adjusted Sea Level']
    reg2 = linregress(x2, y2)
    x_pred2 = pd.Series([i for i in range(2000, 2050)])
    y_pred2 = reg2.slope * x_pred2 + reg2.intercept
    plt.plot(x2, y2, 'green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (Inches)')
    ax.set_title('Rise In Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()