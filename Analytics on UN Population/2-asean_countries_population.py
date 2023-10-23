import csv
import matplotlib.pyplot as plt
from main import ASEAN_Countries,population_reader


def execute():
    # Dictionary to store population of ASEAN countries
    population={}
    for row in population_reader:
        year = row['Year']
        country=row['Region']
        if year == '2014' and country in ASEAN_Countries:
                population[country]=row['Population']            
                
    for i in population:
        print(i," : ",population[i])
    return population


def plot(population):
    # Plotting the bar graph
    plt.bar(population.keys(),population.values())
    plt.xlabel('ASEAN_Countries')
    plt.xticks(rotation=90)
    plt.ylabel('Population')
    plt.title('For the year 2014. Bar Chart of population of ASEAN countries')
    plt.show()
    

population = execute()
plot(population)