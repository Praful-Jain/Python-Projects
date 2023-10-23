import csv
import matplotlib.pyplot as plt
from main import population_reader


def execute():
    # Dictionary to store Indian population over the years
    india_population={}
    for row in population_reader:
        country = row['Region']
        if country=='India':    
            year = row['Year']
            india_population[year]=row['Population']
                
    for i in india_population:
        print(i," : ",india_population[i])
    return india_population
    
    
def plot(india_population): 
    # Plotting the bar graph
    plt.bar(india_population.keys(),india_population.values())
    plt.xlabel('Year')
    plt.xticks(rotation=90)
    plt.ylabel('Population')
    plt.title('India population over years.')
    plt.show()
    
    
india_population = execute()
plot(india_population)