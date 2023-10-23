import csv
import matplotlib.pyplot as plt

def read_file(csv_file):

    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        deliveries_reader = list(csv_reader)  
    return deliveries_reader

def execute(deliveries_reader):
    # will store total runs of teams
    total_runs = {}        

    # Iterate through the rows in the CSV file.
    for row in deliveries_reader :
        if row['batting_team'] in total_runs :
            total_runs[row['batting_team']] += int(row['total_runs'])
        else:
            total_runs[row['batting_team']] = int(row['total_runs'])
            
    print(total_runs)
    return total_runs

def plot(total_runs):
    # Plotting the bar graph
    plt.bar(total_runs.keys(),total_runs.values())
    plt.xlabel('Team')
    plt.xticks(rotation=90)
    plt.ylabel('Runs')
    plt.title('Runs scored by each team')
    plt.show()
    
    
deliveries_reader = read_file('IPL dataset analytics/deliveries.csv')
total_runs = execute(deliveries_reader)
plot(total_runs)