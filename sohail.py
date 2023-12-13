# -*- coding: utf-8 -*-
"""
Name: Shaik Mohammed Sohail
Student ID: 
Course: 7PAM2000-0901-2023 - Applied Data Science 1
University: Msc Data Science (SW) with Placement Year
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def readFile(filename):
    '''
    Parameters
    ----------
    filename: The filename is an argument parsed from the main function which name/path of the csv file

    Returns
    -------
    This function reads the csv file and filters the data and transpose it and returns the respective data frames
    '''
    
    db = pd.read_csv(filename,skiprows = 3)
    db.set_index('Country Name', inplace=True)
    
    db_f = db[db["Indicator Code"] == "ER.H2O.FWTL.ZS"]
    db_p = db[db["Indicator Code"] == "SP.POP.TOTL"]
    
    period = ["2000","2002","2004","2006","2008","2010","2012","2014","2016","2018"]
    
    db_fw = db_f[period]
    db_pg = db_p[period]
    
    db_fw = db_fw.loc[["United Kingdom", "China", "United States", "India"]]
    db_pg = db_pg.loc[["United Kingdom", "China", "United States", "India"]]
    
    db_fw_T = db_fw.transpose()
    db_pg_T = db_pg.transpose()
    
    db_fw.info()
    db_fw.describe()
    db_fw_T.describe()
    
    db_pg.info()
    db_pg.describe()
    
    return db_fw, db_fw_T, db_pg, db_pg_T

def Line(data, data1):
    '''
    Parameters
    ----------
    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the Line graph for the parsed data frame.
    '''
    data.plot(kind="line", figsize=(10, 5))
    plt.title("Annual freshwater withdrawals, total (% of internal resources)")
    plt.xlabel("Year")
    plt.ylabel("Percentage of total withdrawl")
    plt.legend()
    plt.show()
    
    data1.plot(kind="line", figsize=(10, 5))
    plt.title("Total Population Growth")
    plt.xlabel("Year")
    plt.ylabel("Count Population Growth")
    plt.legend()
    plt.show()



def heatmap(file, country):
    # Selecting the indicators which could be the correlation to one another
    indicators = ['EN.ATM.NOXE.ZG', 'EN.ATM.METH.ZG', 'EN.ATM.GHGT.ZG', 'EN.ATM.GHGO.ZG']

    # Get the data from the World Bank dataset
    data = pd.read_csv(file, skiprows=(3))

    # Clean and format the data for the specified country and required indicators
    data = data.loc[data['Country Name'] == country]
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:, ["Indicator Name", "2001","2002","2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"]]

    # Drop non-numeric rows
    data = data.dropna(subset=["2001","2002","2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"], how="any", axis=0)

    # Set "Indicator Name" as index
    data.set_index("Indicator Name", inplace=True)

    # Transpose the data for plotting
    data_transposed = data.transpose()

    # Convert data to numeric (excluding the "Country Name" column)
    data_transposed = data_transposed.apply(pd.to_numeric, errors='coerce')

    # Plotting heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(data_transposed.corr(), annot=True, fmt='.2f', cmap='YlGnBu')

    # Add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Indicator')
    plt.ylabel('Year')

    # Show the plot
    plt.show()       
    

def Bar(data,data1):
    '''

    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the bar graph for the parsed data frame.

    '''
    data = data.loc[:,["2000","2006","2012","2018"]]
    data1 = data1.loc[:,["2000","2006","2012","2018"]]
    
    data.plot(kind="bar", figsize=(10, 5))
    plt.title("Annual freshwater withdrawals, total (% of internal resources)")
    plt.xlabel("Countries")
    plt.ylabel("Percentage of total withdrawl")
    plt.legend()
    plt.show()
    
    data1.plot(kind="bar", figsize=(10, 5))
    plt.title("Total Population Growth")
    plt.xlabel("Countries")
    plt.ylabel("Count Population Growth")
    plt.legend()
    plt.show()

#Main Function
file = "API_19_DS2_en_csv_v2_6183479.csv"
db_Fw, db_Fw_T, db_Pg, db_Pg_T = readFile(file)

Bar(db_Fw,db_Pg)
Line(db_Fw_T, db_Pg_T)

heatmap(file, 'India')
heatmap(file, 'China')
heatmap(file, 'United Kingdom')
heatmap(file,'United States')

