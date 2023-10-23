import csv
import matplotlib.pyplot as plt

def read_file(csv_file):
    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        match_reader = list(csv_reader)  
    return match_reader


def execute(match_reader):        
    extra_runs = {}
    
    for row in match_reader :
        if(row['season'] == '2016') :
            extra_runs[row['winner']] =  extra_runs.get(row['winner'] , 0) + int(row['win_by_runs'])
        
    for i in extra_runs:
        print(i , " : " , extra_runs[i])
    return extra_runs

def plot(extra_runs):
    # Plotting the bar graph
    plt.bar(extra_runs.keys(),extra_runs.values())
    plt.xlabel('Team name')
    plt.xticks(rotation=90)
    plt.ylabel('Extra runs scored')
    plt.title('Extra runs conceded per team in the year 2016')
    plt.show()
    

match_reader = read_file('IPL dataset analytics/matches.csv')
extra_runs = execute(match_reader)
plot(extra_runs)