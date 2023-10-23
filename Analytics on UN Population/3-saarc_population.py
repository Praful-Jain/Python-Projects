import csv
import matplotlib.pyplot as plt
from main import population_reader,ASEAN_Countries

def execute():
    # Dictionary to store population of SAARC countries
    population = {}
    for row in population_reader:
        year = row['Year']
        country = row['Region']
        if country in ASEAN_Countries:
            if year not in population:
                population[year] = 0.0
            population[year] += float(row['Population'])

    for i in population:
        population[i] = round(population[i],3)
        print(i," : ",population[i])
    return population


def plot(population):
    # Plotting the bar graph
    plt.bar(population.keys(),population.values())
    plt.xlabel('Year')
    plt.xticks(rotation=90)
    plt.ylabel('TOTAL population of SAARC countries')
    plt.title('Over the years, TOTAL population of SAARC countries')
    plt.show()
    

population = execute()
plot(population)