import csv
import matplotlib.pyplot as plt
from main import population_reader,ASEAN_Countries


def execute():
    asean_population = { key : [] for key in ASEAN_Countries}

    # Dictionary to store ASEAN countries population over the years
    population = {}
    for row in population_reader:
        year = row['Year']
        country = row['Region']
        if year >= '2004' and year <= '2014' and country in ASEAN_Countries:
            asean_population[country].append(float(row['Population']))
            
    asean_population = {key: value for key, value in asean_population.items() if value}

    for country in asean_population:
        print(country , "-----")
        print(asean_population[country])
        print()
    return asean_population


def plot(asean_population):        
    # Plotting the grouped bar chart
    countries = list(asean_population.keys())
    years = range(2004, 2015)

    # Setting the positions and width for the bars
    pos = list(range(len(years)))
    w = 0.1

    # Creating the grouped bar chart
    for i, country in enumerate(countries):
        plt.bar([p + w * i for p in pos], asean_population[country], width=w, label=country)

    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('ASEAN Countries Population Over the Years (2004-2014)')
    plt.xticks([p + w * (len(countries) / 2 - 0.5) for p in pos], years)
    plt.legend()
    plt.show()
    
    
asean_population = execute()
plot(asean_population)